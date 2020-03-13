# Created by Adam Thompson-Sharpe on 12/03/2020.
import configparser
import requests
from bs4 import BeautifulSoup

from .competition_min import *
from .exceptions import *

class WCA(object):
    """
    Main class to interact with WCA.

    `section_name: str` - The name of the section to find in `pywca.ini`. Should contain at least `username` and `password` fields.
    """
    def __init__(self, section_name: str=None, **kwargs):
        params = {}
        if section_name is not None:
            # Check type
            if type(section_name) is not str:
                raise TypeError(f"Expected str for section_name, got {type(section_name).__name__}.")

            ini = configparser.ConfigParser()
            ini.read("pywca.ini")

            # Check if section provided exists
            if section_name not in ini:
                raise InitError(f"Section {section_name} not found in pywca.ini")

            params = {**dict(ini[section_name]), **kwargs}
        else:
            params = kwargs
        
        # Check parameters
        if "anonymous" in params:
            if params["anonymous"] == True:
                self._anonymous = True
            else:
                self._anonymous = False
                if "username" not in params or "password" not in params:
                    raise InitError("username and password must be supplied if not in anonymous mode, but at least one was not.")
        else:
            self._anonymous = False
            if "username" not in params or "password" not in params:
                    raise InitError("username and password must be supplied if not in anonymous mode, but at least one was not.")
        
        # Set up headers
        if "user_agent" in params:
            self._headers = {"user-agent": params["user_agent"]}
        else:
            self._headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

        # Set up session
        self._s = requests.Session()

        # Do not attempt login if anonymous
        if not self._anonymous:
            # Get CSRF Token
            request_url = "https://www.worldcubeassociation.org/users/sign_in"
            r = self._s.get(request_url, headers=self._headers)
            soup = BeautifulSoup(r.content, "html.parser")

            token = soup.find("meta", {"name": "csrf-token"})["content"]

            data = {"utf-8": "\u2713", "authenticity_token": token, "user[login]": params["username"], "user[password]": params["password"], "user[remember_me]": 0, "commit": "Sign in"}
            r = self._s.post(request_url, data=data, headers=self._headers)
            
            # Check if login was successful
            soup = BeautifulSoup(r.content, "html.parser")

            # Failed login banner is present
            if soup.find("div", {"class": "alert alert-danger alert-dismissible"}) is not None:
                raise AuthError("Initial login failed.")
    
    def get_competitions(self, region: str="all", search: str="", state: str="present", year: str="all years", from_date: str="", to_date: str="", delegate: str=""):
        """
        Get a list of competitions.

        `region: str` - The region to filter by. Continents **must** start with `_`.

        `search: str` - A search term to filter by.

        `state: str` - Either `"present"` or `"recent"` depending on what competitions to view.
        """
        # Request parameters
        params = {"utf8": "\u2713", "region": region, "search": search, "state": state, "year": year, "from_date": from_date, "to_date": to_date, "delegate": delegate, "display": "list"}
        request_url = "https://www.worldcubeassociation.org/competitions"

        # Get competitions page
        r = self._s.get(request_url, params=params, headers=self._headers)
        soup = BeautifulSoup(r.content, "html.parser")

        # Iterate through competitions
        for comp in soup.find("div", {"id": "upcoming-comps"}).find("ul").findAll("li", {"class": "not-past"}):
            # Get competition info
            comp_info = comp.find("span", {"class": "competition-info"})

            # Get competition name/url
            comp_a = comp_info.find("div", {"class": "competition-link"}).find("a")
            comp_name = str(next(comp_a.strings))
            comp_url = "https://www.worldcubeassociation.org" + comp_a.get("href")

            # Get competition location
            comp_loc = "".join(list(comp_info.find("div", {"class": "location"}).strings)[1:3]).strip()
            
            # Get venue
            comp_venue_div = comp_info.find("div", {"class": "venue-link"})
            comp_venue_url = None
            if comp_venue_div.find("a") is not None:
                comp_venue_url = comp_venue_div.find("a").get("href")
            
            comp_venue = str(list(comp_venue_div.strings)[1])

            yield CompetitionMin(comp_name, comp_url, comp_loc, comp_venue, comp_venue_url)

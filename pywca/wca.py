# Created by Adam Thompson-Sharpe on 12/03/2020.
import configparser
import requests
from bs4 import BeautifulSoup

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
            if params["anonymous"] != True:    
                if "username" not in params or "password" not in params:
                    raise InitError("username and password must be supplied if not in anonymous mode, but at least one was not.")
        
        # Set up headers
        if "user_agent" in params:
            self._headers = {"user-agent": params["user_agent"]}
        else:
            self._headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

        # Set up session
        self._s = requests.Session()

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

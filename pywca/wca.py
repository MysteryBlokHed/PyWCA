# Created by Adam Thompson-Sharpe on 12/03/2020.
from bs4 import BeautifulSoup
from configparser import ConfigParser
from requests import Session

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

            ini = ConfigParser()
            ini.read("pywca.ini")

            # Check if section provided exists
            if section_name not in ini:
                raise InitError(f"Section {section_name} not found in pywca.ini")

            params = {**dict(ini), **kwargs}
        else:
            params = kwargs
        
        # Check parameters
        if "anonymous" in params:
            if params["anonymous"] != True:    
                if "username" not in params or "password" not in params:
                    raise InitError("username and password must be supplied if not in anonymous mode, but at least one was not.")
                
                    
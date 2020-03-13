# Created by Adam Thompson-Sharpe on 12/03/2020.
class CompetitionMin(object):
    def __init__(self, name: str, url: str, geo_location: str, venue: str, venue_site: str=None):
        # Check types
        if type(name) is not str:
            raise TypeError(f"Expected str for name, got {type(name).__name__}.")
        if type(url) is not str:
            raise TypeError(f"Expected str for url, got {type(name).__name__}.")
        if type(geo_location) is not str:
            raise TypeError(f"Expected str for geo_location, got {type(geo_location).__name__}.")
        if type(venue) is not str:
            raise TypeError(f"Expected str for venue, got {type(venue).__name__}.")
        if type(venue_site) not in (str, type(None)):
            raise TypeError(f"Expected str for venue_site, got {type(venue_site).__name__}.")

        self._name = name
        self._url = url
        self._geo_location = geo_location
        self._venue = venue
        self._venue_site = venue_site

    def __getitem__(self, key: str):
        if key == "name":
            return self._name
        elif key == "url":
            return self._url
        elif key == "geo_location":
            return self._geo_location
        elif key == "venue":
            return self._venue
        elif key == "venue_site":
            return self._venue_site

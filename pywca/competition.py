# Created by Adam Thompson-Sharpe on 12/03/2020.
class CompetitionMin(object):
    """
    A minimal Competition object.

    `name: str` - The name of the competition.

    `url: str` - The url of the competition on the WCA website.

    `geo_location: str` - The city/country of the competition (eg. Columbus, Ohio, United States)

    `venue: str` - The venue the competition is/was at.

    `date: str` - The date of the competition, formatted as Month Day, Year, or Month Day - Day, Year (eg. Mar 14, 2020, Mar 13 - 15, 2020)

    `venue_site: str` - The website of the competition venue (NOT the address map link)
    """
    def __init__(self, name: str, url: str, geo_location: str, venue: str, date: str, venue_site: str=None):
        # Check types
        if type(name) is not str:
            raise TypeError(f"Expected str for name, got {type(name).__name__}.")
        if type(url) is not str:
            raise TypeError(f"Expected str for url, got {type(name).__name__}.")
        if type(geo_location) is not str:
            raise TypeError(f"Expected str for geo_location, got {type(geo_location).__name__}.")
        if type(venue) is not str:
            raise TypeError(f"Expected str for venue, got {type(venue).__name__}.")
        if type(date) is not str:
            raise TypeError(f"Expected str for date, got {type(date).__name__}.")
        if type(venue_site) not in (str, type(None)):
            raise TypeError(f"Expected str for venue_site, got {type(venue_site).__name__}.")
        
        # Set variables
        self._name = name
        self._url = url
        self._geo_location = geo_location
        self._venue = venue
        self._date = date
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
        elif key == "date":
            return self._date
        elif key == "venue_site":
            return self._venue_site
        else:
            raise KeyError(key)

class Competition(object):
    """
    A detailed Competition object.

    `name: str` - The name of the competition.

    `url: str` - The url of the competition on the WCA website.

    `geo_location: str` - The city/country of the competition (eg. Columbus, Ohio, United States)

    `venue: str` - The venue the competition is/was at.

    `date: str` - The date of the competition, formatted as Month Day, Year, or Month Day - Day, Year (eg. Mar 14, 2020, Mar 13 - 15, 2020)

    `address: str` - The address of the venue for the competition.

    `address_map_link: str` - The Google Maps link to the address.

    `organizers: str` - The organizers of the competition (eg. `"John Doe, Jack Doe and Jack"`, `"Lorem Ipsum"`)

    `delegates: str` - The WCA delegates at the competition (eg. `"John Doe, Jack Doe and Jack"`, `"Lorem Ipsum"`)

    `events: list` - The events at the competition (eg. `["3x3x3 Cube", "3x3x3 Blindfolded"]`)

    `main_event: str` - The main event at the competition (if one is listed) (eg. `"3x3x3 Cube"`)

    `venue_site: str` - The website of the competition venue (NOT the address map link)
    """
    def __init__(self, name: str, url: str, geo_location: str, venue: str, date: str, address: str, address_map_link: str, organizers: str, delegates: str, events: list, main_event: str=None, venue_site: str=None):
        # Check types
        if type(name) is not str:
            raise TypeError(f"Expected str for name, got {type(name).__name__}.")
        if type(url) is not str:
            raise TypeError(f"Expected str for url, got {type(url).__name__}.")
        if type(geo_location) is not str:
            raise TypeError(f"Expected str for geo_location, got {type(geo_location).__name__}.")
        if type(venue) is not str:
            raise TypeError(f"Expected str for venue, got {type(venue).__name__}.")
        if type(date) is not str:
            raise TypeError(f"Expected str for date, got {type(date).__name__}.")
        if type(address) is not str:
            raise TypeError(f"Expected str for address, got {type(address).__name__}.")
        if type(address_map_link) is not str:
            raise TypeError(f"Expected str for address_map_link, got {type(address_map_link).__name__}.")
        if type(organizers) is not str:
            raise TypeError(f"Expected str for organizers, got {type(organizers).__name__}.")
        if type(delegates) is not str:
            raise TypeError(f"Expected str for delegates, got {type(delegates).__name__}.")
        if type(events) is not list:
            raise TypeError(f"Expected list for events, got {type(events).__name__}.")
        if type(main_event) not in (str, type(None)):
            raise TypeError(f"Expected str for main_event, got {type(main_event).__name__}.")
        if type(venue_site) not in (str, type(None)):
            raise TypeError(f"Expected str for venue_site, got {type(venue_site).__name__}.")
        
        # Set variables
        self._name = name
        self._url = url
        self._geo_location = geo_location
        self._venue = venue
        self._date = date
        self._address = address
        self._address_map_link = address_map_link
        self._organizers = organizers
        self._delegates = delegates
        self._events = events
        self._main_event = main_event
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
        elif key == "date":
            return self._date
        elif key == "address":
            return self._address
        elif key == "address_map_link":
            return self._address_map_link
        elif key == "organizers":
            return self._organizers
        elif key == "delegates":
            return self._delegates
        elif key == "events":
            return self._events
        elif key == "main_event":
            return self._main_event
        elif key == "venue_site":
            return self._venue_site
        else:
            raise KeyError(key)

class Location:
    """
    Represents a generic Location.

    Attributes:
        _location_id (int): The unique ID of the location.
        _name (str): The name of the location.
        _cardinal_description_text (str): A short description of what the location looks like from afar.
        _location_description_text (str): A longer description for when the player is in the location.
        _discovered_status (bool): Has the player been there before.
        locations (list): A list of all created Location objects.
    """
    locations = list()

    def __init__(self, location_id: int, name: str, cardinal_description_text: str, location_description_text: str):
        """
        Initialize a new Location.

        Arguments:
            location_id (int): The unique ID of the location.
            name (str): The name of the location.
            cardinal_description_text (str): A short description of what the location looks like from afar.
            location_description_text (str): A longer description for when the player is in the location.
        """
        self._location_id = location_id
        self._name = name
        self._cardinal_description_text = cardinal_description_text
        self._location_description_text = location_description_text
        self._discovered_status = False
        self.locations.append(self)

    def get_location_id(self):
        return self._location_id

    def get_cardinal_description_text(self):
        return self._cardinal_description_text

    def get_location_description_text(self):
        return self._location_description_text

    def get_discovery_status(self):
        return self._discovered_status

    def location_discovered(self):
        self._discovered_status = True


class SeaLocation(Location):
    """
    Represents a Sea Location.

    Attributes:
        _location_id (int): The unique ID of the location.
        name (str): The name of the location.
        _cardinal_description_text (str): A short description of what the location looks like from afar.
        _location_description_text (str): A longer description for when the player is in the location.
        _discovered_status (bool): Has the player been there before.
    """
    def __init__(self, location_id: int, name: str, cardinal_description_text: str, location_description_text: str):
        super().__init__(location_id, name, cardinal_description_text, location_description_text)
        """
        Initialize a new Sea Location.

        Arguments:
            location_id (int): The unique ID of the location.
            name (str): The name of the location.
            cardinal_description (str): A short description of what the location looks like from afar.
            location_description (str): A longer description for when the player is in the location.
        """


class ExplorableLocation(Location):
    """
    Represents an Explorable Location.

    Attributes:
        _location_id (int): The unique ID of the location.
        name (str): The name of the location.
        north (int): The ID for the location to the North.
        east (int): The ID for the location to the East.
        south (int): The ID for the location to the South.
        west (int): The ID for the location to the West.
        _cardinal_description_text (str): A short description of what the location looks like from afar.
        _location_description_text (str): A longer description for when the player is in the location.
        _discovered_status (bool): Has the player been there before.
    """
    def __init__(self, location_id: int, name: str, north: int, east: int, south: int, west: int,
                 cardinal_description_text: str, location_description_text: str):
        super().__init__(location_id, name, cardinal_description_text, location_description_text)
        """
        Initialize an Explorable Location.

        Arguments:
            location_id (int): The unique ID of the location.
            name (str): The name of the location.
            north (int): The ID for the location to the North.
            east (int): The ID for the location to the East.
            south (int): The ID for the location to the South.
            west (int): The ID for the location to the West.
            cardinal_description (str): A short description of what the location looks like from afar.
            location_description (str): A longer description for when the player is in the location.
        """
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self._location_items = list()

    def add_item_to_location(self, item):
        if item is not None:
            self._location_items.append(item)

    def get_location_items(self):
        return self._location_items

    def remove_location_item(self, item):
        if item is not None:
            for location_item in self._location_items:
                if item == location_item:
                    self._location_items.remove(item)


class StartLocation(ExplorableLocation):
    def __init__(self, location_id: int, name: str, north: int, east: int, south: int, west: int,
                 cardinal_description_text: str, location_description_text: str, start_text: str):
        """

        :param location_id:
        :param name:
        :param north:
        :param east:
        :param south:
        :param west:
        :param cardinal_description_text:
        :param location_description_text:
        :param start_text:
        """
        super().__init__(location_id, name, north, east, south, west, cardinal_description_text,
                         location_description_text)
        self._start_text = start_text

    def get_start_text(self):
        return self._start_text

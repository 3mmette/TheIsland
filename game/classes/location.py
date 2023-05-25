class Location:
    """
    This class represents a generic location that all other game_files inherit off.
    It keeps track of all created location classes.
    It has the following attributes.
        _location_id (int): The unique ID of the location.
        _name (str): The name of the location.
        _cardinal_description_text (str): A short description of what the location looks like from afar.
        _location_description_text (str): A longer description for when the player is in the location.
        _discovered_status (bool): Has the player been there before.
    """
    locations = list()

    def __init__(self, location_id: int, name: str, cardinal_description_text: str, location_description_text: str):
        """
        Initialize a new location.
        :param location_id: The unique ID of the location.
        :param name: The name of the location.
        :param cardinal_description_text: A short description of what the location looks like from afar.
        :param location_description_text: A longer description for when the player is in the location.
        """
        self._location_id = location_id
        self._name = name
        self._cardinal_description_text = cardinal_description_text
        self._location_description_text = location_description_text
        self._discovered_status = False
        self.locations.append(self)
        self.locations.sort(key=lambda x: x.get_location_id())

    def get_location_id(self):
        """
        Gets the unique ID of the location.
        :return: The game_files unique ID.
        """
        return self._location_id

    def get_name(self):
        """
        Gets the name of the location.
        :return: The name.
        """
        return self._name

    def get_cardinal_description_text(self):
        """
        Gets the short description of what the location looks like from afar.
        :return: The short description.
        """
        return self._cardinal_description_text

    def get_location_description_text(self):
        """
        Gets the longer description for when the player is in the location.
        :return: The longer description.
        """
        return self._location_description_text

    def get_discovery_status(self):
        """
        Gets the discovery status of the location.
        :return: If it has been discovered or not.
        """
        return self._discovered_status

    def location_discovered(self):
        """
        Sets the discovery status to True when a location is discovered.
        """
        self._discovered_status = True


class SeaLocation(Location):
    """
    This class represents a sea location that inherits from location.
    It has the following attributes.
        _location_id (int): The unique ID of the location.
        _name (str): The name of the location.
        _cardinal_description_text (str): A short description of what the location looks like from afar.
        _location_description_text (str): A longer description for when the player is in the location.
        _discovered_status (bool): Has the player been there before.
    """
    def __init__(self, location_id: int, name: str, cardinal_description_text: str, location_description_text: str):
        """
        Initialize a new sea location.
        :param location_id: The unique ID of the location.
        :param name: The name of the location.
        :param cardinal_description_text: A short description of what the location looks like from afar.
        :param location_description_text: A longer description for when the player is in the location.
        """
        super().__init__(location_id, name, cardinal_description_text, location_description_text)


class ExplorableLocation(Location):
    """
    This class represents an explorable location that inherits from location.
    It has the following attributes.
        _location_id (int): The unique ID of the location.
        _name (str): The name of the location.
        _north_id (int): The ID for the location to the North.
        _east_id (int): The ID for the location to the East.
        _south_id (int): The ID for the location to the South.
        _west_id (int): The ID for the location to the West.
        _cardinal_description_text (str): A short description of what the location looks like from afar.
        _location_description_text (str): A longer description for when the player is in the location.
        _discovered_status (bool): Has the player been there before.
        _location_items (list): Contains all the base classes in the location.
    """
    explorable_locations = list()

    def __init__(self, location_id: int, chart_location_byte: int, name: str, north_id: int, east_id: int, south_id: int, west_id: int,
                 cardinal_description_text: str, location_description_text: str):
        """
        Initialize a new explorable location.
        :param location_id: The unique ID of the location.
        :param name: The name of the location.
        :param north_id: The ID for the location to the North.
        :param east_id: The ID for the location to the East.
        :param south_id: The ID for the location to the South.
        :param west_id: The ID for the location to the West.
        :param cardinal_description_text: A short description of what the location looks like from afar.
        :param location_description_text: A longer description for when the player is in the location.
        """
        super().__init__(location_id, name, cardinal_description_text, location_description_text)
        self._chart_location_byte = chart_location_byte
        self._north_id = north_id
        self._east_id = east_id
        self._south_id = south_id
        self._west_id = west_id
        self._location_items = list()
        self.explorable_locations.append(self)
        self.explorable_locations.sort(key=lambda x: x.get_location_id())

    def get_chart_location_byte(self):
        """
        Gets the number of bytes needed to access the correct location on the chart.
        :return: The number of bytes.
        """
        return self._chart_location_byte

    def get_north_id(self):
        """
        Gets the location ID of the location to the north.
        :return: The location ID.
        """
        return self._north_id

    def get_east_id(self):
        """
        Gets the location ID of the location to the east.
        :return: The location ID.
        """
        return self._east_id

    def get_south_id(self):
        """
        Gets the location ID of the location to the south.
        :return: The location ID.
        """
        return self._south_id

    def get_west_id(self):
        """
        Gets the location ID of the location to the west.
        :return: The location ID.
        """
        return self._west_id

    def add_item_to_location(self, item):
        """
        Adds the item to the list of items in the location.
        """
        if item is not None:
            self._location_items.append(item)

    def get_location_items(self):
        """
        Gets the list of items in the location.
        :return: The list.
        """
        return self._location_items

    def remove_location_item(self, item):
        """
        If the item is not none and is in the list of items in the location.
        Removes the item.
        """
        if item is not None:
            for location_item in self._location_items:
                if item == location_item:
                    self._location_items.remove(item)

    def clear_location_items(self):
        """
        Clears all items from a location to reset.
        """
        self._location_items.clear()


class StartLocation(ExplorableLocation):
    """
    This class represents the start location that inherits from explorable location.
    It has the following attributes.
        _location_id (int): The unique ID of the location.
        _name (str): The name of the location.
        _north_id (int): The ID for the location to the North.
        _east_id (int): The ID for the location to the East.
        _south_id (int): The ID for the location to the South.
        _west_id (int): The ID for the location to the West.
        _cardinal_description_text (str): A short description of what the location looks like from afar.
        _location_description_text (str): A longer description for when the player is in the location.
        _start_text (str): An initial longer description for when the player starts the game.
        _discovered_status (bool): Has the player been there before.
        _location_items (list): Contains all the base classes in the location.
    """
    def __init__(self, location_id: int, chart_location_byte: int, name: str, north_id: int, east_id: int, south_id: int, west_id: int,
                 cardinal_description_text: str, location_description_text: str, start_text: str):
        """
        Initialize a new start location.
        :param location_id: The unique ID of the location.
        :param name: The name of the location.
        :param north_id: The ID for the location to the North.
        :param east_id: The ID for the location to the East.
        :param south_id: The ID for the location to the South.
        :param west_id: The ID for the location to the West.
        :param cardinal_description_text: A short description of what the location looks like from afar.
        :param location_description_text: A longer description for when the player is in the location.
        :param start_text: An initial longer description for when the player starts the game.
        """
        super().__init__(location_id, chart_location_byte,  name, north_id, east_id, south_id, west_id, cardinal_description_text,
                         location_description_text)
        self._start_text = start_text

    def get_start_text(self):
        """
        Gets the initial longer description for when the player starts the game.
        :return: The initial longer description.
        """
        return self._start_text

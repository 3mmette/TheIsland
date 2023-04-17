class Location:
    """
    Represents a generic Location.

    Attributes:
        location_id (int): The unique ID of the location.
        name (str): The name of the location.
        cardinal_description (str): A short description of what the location looks like from afar.
        location_description (str): A longer description for when the player is in the location.
        discovered (bool): Has the player been there before.
        locations (list): A list of all created Location objects.
    """
    locations = list()

    def __init__(self, location_id: int, name: str, cardinal_description: str, location_description: str):
        """
        Initialize a new Location.

        Arguments:
            location_id (int): The unique ID of the location.
            name (str): The name of the location.
            cardinal_description (str): A short description of what the location looks like from afar.
            location_description (str): A longer description for when the player is in the location.
        """
        self.location_id = location_id
        self.name = name
        self.cardinal_description = cardinal_description
        self.location_description = location_description
        self.discovered = False
        self.locations.append(self)


class SeaLocation(Location):
    """
    Represents a Sea Location.

    Attributes:
        location_id (int): The unique ID of the location.
        name (str): The name of the location.
        cardinal_description (str): A short description of what the location looks like from afar.
        location_description (str): A longer description for when the player is in the location.
        discovered (bool): Has the player been there before.
    """
    def __init__(self, location_id: int, name: str, cardinal_description: str, location_description: str):
        super().__init__(location_id, name, cardinal_description, location_description)
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
        location_id (int): The unique ID of the location.
        name (str): The name of the location.
        north (int): The ID for the location to the North.
        east (int): The ID for the location to the East.
        south (int): The ID for the location to the South.
        west (int): The ID for the location to the West.
        cardinal_description (str): A short description of what the location looks like from afar.
        location_description (str): A longer description for when the player is in the location.
        discovered (bool): Has the player been there before.
    """
    def __init__(self, location_id: int, name: str, north: int, east: int, south: int, west: int,
                 cardinal_description: str, location_description: str):
        super().__init__(location_id, name, cardinal_description, location_description)
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
        self.items = list()


class StartLocation(ExplorableLocation):
    def __init__(self, location_id: int, name: str, north: int, east: int, south: int, west: int,
                 cardinal_description: str, location_description: str, start_text: str):
        """

        :param location_id:
        :param name:
        :param north:
        :param east:
        :param south:
        :param west:
        :param cardinal_description:
        :param location_description:
        :param start_text:
        """
        super().__init__(location_id, name, north, east, south, west, cardinal_description, location_description)

        self.start_text = start_text

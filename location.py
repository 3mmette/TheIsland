class Location:
    # Create a list off all created locations.
    locations = list()

    def __init__(self, location_id: int, cardinal_description: str, location_description: str):
        self.location_id = location_id
        self.discovered = False
        self.cardinal_description = cardinal_description
        self.location_description = location_description
        self.locations.append(self)


class SeaLocation(Location):

    def __init__(self, location_id, cardinal_description, location_description):
        super().__init__(location_id, cardinal_description, location_description)


class ExplorableLocation(Location):
    def __init__(self, location_id, north, east, south, west, cardinal_description, location_description):
        super().__init__(location_id, cardinal_description, location_description)
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.items = list()
        self.dropped_items = list()


class StartLocation(ExplorableLocation):
    def __init__(self, location_id, north, east, south, west, cardinal_description, location_description, start_text):
        super().__init__(location_id, north, east, south, west, cardinal_description, location_description)
        self.start_text = start_text

    def print_start_text(self):
        print(self.start_text)

class Location:
    # Create a list off all created locations.
    locations = list()

    def __init__(self, location_id, short_description, long_description):
        self.location_id = location_id
        self.discovered = False
        self.short_description = short_description
        self.long_description = long_description
        self.locations.append(self)


class SeaLocation(Location):
    sea_locations = list()

    def __init__(self, location_id, short_description, long_description):
        super().__init__(location_id, short_description, long_description)
        self.sea_locations.append(self)


class ExplorableLocation(Location):
    def __init__(self, location_id, north, east, south, west, short_description, long_description):
        super().__init__(location_id, short_description, long_description)
        self.north = north
        self.east = east
        self.south = south
        self.west = west


class StartLocation(ExplorableLocation):
    def __init__(self, location_id, north, east, south, west, short_description, long_description, start_text):
        super().__init__(location_id, north, east, south, west, short_description, long_description)
        self.start_text = start_text

    def print_start_text(self):
        print(self.start_text)


from game.classes.location import ExplorableLocation


class Chart:
    """
    This class represents a chart that tracks locations that have been discovered and the players' location.
    It uses a random access technique to read and write to a file.
    It has the following attributes.
        _file_name (str): The name of the file to read and write to.
        _extra_bytes_to_current_location_mark (int): Number of bytes to the current location mark.
        _bytes_for_location_name (int): Number of bytes the location name must take up.
    """
    def __init__(self):
        """
        Initialize a new chart. All parameters are prefilled.
        """
        self._file_name = "game/game_files/chart.txt"
        self._extra_bytes_to_current_location_mark = 15
        self._bytes_for_location_name = 14

    def get_file_name(self):
        """
        Gets the file name to read and write to.
        :return: The files name.
        """
        return self._file_name

    def get_extra_bytes_to_current_location_mark(self):
        """
        Gets the additional bytes need to reach the current location mark.
        :return: The number of bytes.
        """
        return self._extra_bytes_to_current_location_mark

    def get_bytes_for_location_name(self):
        """
        Gets the number of bytes needed to ensure default unknown location is overwritten.
        :return: The number of bytes.
        """
        return self._bytes_for_location_name

    def show_chart(self):
        """
        Reads the file and creates a string to display the chart.
        :return: The string.
        """
        file = open(self.get_file_name(), "r")
        chart_string = file.read()
        file.close()
        return chart_string

    def location_discovered(self, location):
        """
        When a new location is discovered, reveals the name of the location and marks the player there.
        :param location: The current location.
        """
        # Is it a location the player can explore.
        if isinstance(location, ExplorableLocation):
            # Get the variables needed.
            location_name = location.get_name()
            spacing = self.get_bytes_for_location_name() - len(location_name)
            chart_index = location.get_chart_location_byte()
            # Writes to chart file.
            with open(self.get_file_name(), "rb+") as file:
                # Location name.
                file.seek(chart_index)
                file.write((location_name + (" " * spacing)).encode())
                # Current location mark.
                file.seek(chart_index + self.get_extra_bytes_to_current_location_mark())
                file.write(b"X")

    def remove_player_location(self, location):
        """
        Before the player moves, removes the location mark from the chart.
        :param location: The current location.
        """
        # Is it a location the player can explore.
        if isinstance(location, ExplorableLocation):
            # Get the variables needed.
            chart_index = location.get_chart_location_byte()
            # Writes to chart file.
            with open(self.get_file_name(), "rb+") as file:
                # Removes location mark.
                file.seek(chart_index + self.get_extra_bytes_to_current_location_mark())
                file.write(b" ")

    def add_player_location(self, location):
        """
        After the player moves, adds the location mark to the chart.
        :param location: The current location.
        """
        # Is it a location the player can explore.
        if isinstance(location, ExplorableLocation):
            # Get the variables needed.
            chart_index = location.get_chart_location_byte()
            # Writes to chart file.
            with open(self.get_file_name(), "rb+") as file:
                # Current location mark.
                file.seek(chart_index + self.get_extra_bytes_to_current_location_mark())
                file.write(b"X")

    def reset_chart(self, locations):
        """
        At the start of the game, resets the chart to ensure all location are unknown land and the is no location mark.
        :param locations: List of all locations.
        """
        # Writes to chart file.
        with open(self.get_file_name(), "rb+") as file:
            # For every location.
            for location in locations:
                # Is it a location the player can explore.
                if isinstance(location, ExplorableLocation):
                    # Unknown land for location name.
                    file.seek(location.get_chart_location_byte())
                    file.write(b"UNKNOWN LAND  ")
                    # Blank for current location.
                    file.seek(location.get_chart_location_byte() + self.get_extra_bytes_to_current_location_mark())
                    file.write(b" ")

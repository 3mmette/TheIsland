from classes.location import ExplorableLocation

class Chart:
    def __init__(self):
        self._file_name = "chart.txt"

    def get_file_name(self):
        return self._file_name

    def show_chart(self):
        chart_string = ""
        file = open(self.get_file_name(), "r")
        for line in file:
            chart_string += f"{line}"
        return chart_string

    def location_discovered(self, location):
        if isinstance(location, ExplorableLocation):
            location_name = location.get_name()
            spacing = 14 - len(location_name)
            chart_index = location.get_chart_location_byte()
            with open(self.get_file_name(), "rb+") as file:
                file.seek(chart_index)
                file.write((location_name + (" " * spacing)).encode())
                file.seek(chart_index + 15)
                file.write(b"X")

    def reset_chart(self, locations):
        for location in locations:
            if isinstance(location, ExplorableLocation):
                with open(self.get_file_name(), "rb+") as file:
                    file.seek(location.get_chart_location_byte())
                    file.write(b"UNKNOWN LAND  ")
                    file.seek(location.get_chart_location_byte() + 15)
                    file.write(b" ")




"""
file = open("game_files/high_scores.txt", "r")

# If the user was using one of the three pre-made word collections.
while count <= 2:
    for line in file.readlines(3):
        count += 1
        
        
# Write the updated scores to file if a new score added.
if place is not None:
    file = open("game_files/high_scores.txt", "w")
    for line in lines:
        file.write(line + "\n")
    file.close()     
"""

from location import *
from item import *
import location_text


loc_zero = StartLocation(0, 1, 13, 13, 13,
                         location_text.location_zero_short,
                         location_text.location_zero_long,
                         location_text.location_zero_start)
loc_one = ExplorableLocation(1, 4, 2, 0, 13,
                             location_text.location_one_short,
                             location_text.location_one_long)
loc_two = ExplorableLocation(2, 5, 3, 13, 1,
                             location_text.location_two_short,
                             location_text.location_two_long)
loc_three = ExplorableLocation(3, 6, 13, 13, 2,
                               location_text.location_three_short,
                               location_text.location_three_long)
loc_four = ExplorableLocation(4, 7, 5, 1, 12,
                              location_text.location_four_short,
                              location_text.location_four_long)
loc_five = ExplorableLocation(5, 8, 6, 2, 4,
                              location_text.location_five_short,
                              location_text.location_file_long)
loc_six = ExplorableLocation(6, 9, 12, 3, 5,
                             location_text.location_six_short,
                             location_text.location_six_long)
loc_seven = ExplorableLocation(7, 11, 8, 4, 12,
                               location_text.location_seven_short,
                               location_text.location_seven_long)
loc_eight = ExplorableLocation(8, 10, 9, 5, 7,
                               location_text.location_eight_short,
                               location_text.location_eight_long)
loc_nine = ExplorableLocation(9, 11, 12, 6, 8,
                              location_text.location_nine_short,
                              location_text.location_nine_long)
loc_ten = ExplorableLocation(10, 11, 11, 8, 11,
                             location_text.location_ten_short,
                             location_text.location_ten_long)
loc_eleven = SeaLocation(11,
                         location_text.location_top_short,
                         location_text.location_top_end)
loc_twelve = SeaLocation(12,
                         location_text.location_side_short,
                         location_text.location_side_end)
loc_thirteen = SeaLocation(13,
                           location_text.location_bottom_short,
                           location_text.location_bottom_end)

hex01 = Item("Hex01", "Hex 1")

if __name__ == '__main__':
    # Starting location.
    current_location = 0

    loc_zero.print_start_text()

    while True:
        # Get the current location information.
        for location in Location.locations:
            if location.location_id == current_location:

                # If you have not been there before.
                print("")
                if not location.discovered:
                    print(f"You arrive at {location.long_description}")
                    location.discovered = True
                # If you have been there before.
                else:
                    print(f"You return to {location.long_description}")

                # Options for movement and prompt.
                print(f"To the North {Location.locations[location.north].short_description}")
                print(f"To the East {Location.locations[location.east].short_description}")
                print(f"To the South {Location.locations[location.south].short_description}")
                print(f"To the West {Location.locations[location.west].short_description}")
                direction = input("Move to? ").strip().upper()

                # Complete movement.
                # Selected North.
                if direction == "N":
                    # If North goes into the sea.
                    if Location.locations[location.north] in SeaLocation.sea_locations:
                        print(Location.locations[location.north].long_description)
                        exit()
                    # If North goes to an explorable location.
                    else:
                        current_location = location.north

                # Selected East.
                elif direction == "E":
                    # If East goes into the sea.
                    if Location.locations[location.east] in SeaLocation.sea_locations:
                        print(Location.locations[location.east].long_description)
                        exit()
                    # If East goes to an explorable location.
                    else:
                        current_location = location.east

                # Selected South.
                elif direction == "S":
                    # If South goes into the sea.
                    if Location.locations[location.south] in SeaLocation.sea_locations:
                        print(Location.locations[location.south].long_description)
                        exit()
                    # If South goes to an explorable location.
                    else:
                        current_location = location.south

                # Selected West.
                elif direction == "W":
                    # If West goes into the sea.
                    if Location.locations[location.west] in SeaLocation.sea_locations:
                        print(Location.locations[location.west].long_description)
                        exit()
                    # If West goes to an explorable location.
                    else:
                        current_location = location.west

                # Z to exit game
                elif direction == "z":
                    exit()

                # Any other input
                else:
                    print("Invalid input")


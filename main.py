from locations.location_zero import *
from locations.location_one import *
from locations.location_two import *
from locations.location_three import *
from locations.location_four import *
from locations.location_five import *
from locations.location_six import *
from locations.location_seven import *
from locations.location_eight import *
from locations.location_nine import *
from locations.location_ten import *
from locations.locations_surrounding import *
from backpack import BackPack

backpack = BackPack(None)

def full_location():
    pass

if __name__ == '__main__':

    for location in ExplorableLocation.locations:
        for item in Item.items:
            if item.location == location.location_id:
                location.items.append(item)

    # Starting location.
    current_location = 0

    while True:
        # Get the current location information.
        for location in Location.locations:
            if location.location_id == current_location:
                move = False

                # If you have not been there before.
                print("")
                if not location.discovered:
                    print(f"You arrive at {location.location_description}")
                    location.discovered = True
                # If you have been there before.
                else:
                    print(f"You return to {location.location_description}")

                # Print the static items into the location.
                for item in location.items:
                    if item.is_visible and type(item) is not Movable:
                        item.discovered = True
                        print(item.location_text)
                # Print the mobile items into the location.
                for item in location.items:
                    if item.is_visible and type(item) is Movable:
                        item.discovered = True
                        print(item.location_text)

                # Print any dropped items into the location.
                if len(location.dropped_items) != 0:
                    print("On the ground lies the dropped ", end="")
                    for item in location.dropped_items:
                        if len(location.dropped_items) == 1:
                            print(f"{item.name}.")
                        else:
                            print(f"{item.name},")

                # Options for movement and prompt.
                print(f"\nTo the North {Location.locations[location.north].cardinal_description}")
                print(f"To the East {Location.locations[location.east].cardinal_description}")
                print(f"To the South {Location.locations[location.south].cardinal_description}")
                print(f"To the West {Location.locations[location.west].cardinal_description}")

                # Input
                while not move:
                    player_input = input("Do what?").strip().upper().split(" ", 1)
                    action = player_input[0]
                    thing = player_input[1]

                    if action == "EXAMINE":
                        for item in Item.items:
                            if thing == item.name:
                                item.Inspect()
                                if item.child:
                                    child = item.child
                                    child.is_visible = True
                                    child.discovered = True

                    if action == "INTERACT":
                        pass

                    if action == "OPEN":
                        if thing == "BAG":
                            print(f"Your BAG currently had {backpack.count()} items.")
                            backpack.list()
                        else:
                            for item in Item.items:
                                if thing == item.name:
                                    try:
                                        item.Open()
                                    except:
                                        print(f"{item.name} cannot be opened.")

                    if action == "CLOSE":
                        for item in Item.items:
                            if thing == item.name:
                                item.Close()

                    if action == "TAKE":
                        for item in Item.items:
                            if thing == item.name:
                                backpack.add(item)

                    if action == "DROP":
                        for item in Item.items:
                            if thing == item.name:
                                backpack.remove(item, Location.locations[current_location])

                    if action == "MOVE":
                        if thing == "N":
                            # If North goes into the sea.
                            if type(Location.locations[location.north]) is SeaLocation:
                                print(Location.locations[location.north].location_description)
                                exit()
                            # If North goes to an explorable location.
                            else:
                                current_location = location.north
                                move = True

                        # Selected East.
                        elif thing == "E":
                            # If East goes into the sea.
                            if type(Location.locations[location.east]) is SeaLocation:
                                print(Location.locations[location.east].location_description)
                                exit()
                            # If East goes to an explorable location.
                            else:
                                current_location = location.east
                                move = True

                        # Selected South.
                        elif thing == "S":
                            # If South goes into the sea.
                            if type(Location.locations[location.south]) is SeaLocation:
                                print(Location.locations[location.south].location_description)
                                exit()
                            # If South goes to an explorable location.
                            else:
                                current_location = location.south
                                move = True

                        # Selected West.
                        elif thing == "W":
                            # If West goes into the sea.
                            if type(Location.locations[location.west]) is SeaLocation:
                                print(Location.locations[location.west].location_description)
                                exit()
                            # If West goes to an explorable location.
                            else:
                                current_location = location.west
                                move = True

                        else:
                            print("Invalid direction.")

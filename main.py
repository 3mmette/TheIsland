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


if __name__ == '__main__':

    backpack = BackPack(None)
    for location in ExplorableLocation.locations:
        for item in Item.items:
            if item.location == location.location_id:
                location.items.append(item)

    # Starting location.
    current_location_index = 0
    current_location = Location.locations[current_location_index]

    while True:
        # Get the current location information.
        for location in Location.locations:
            if location.location_id == current_location_index:
                move = False

                # For undiscovered locations (You arrive at...)
                print("")
                if not location.discovered:
                    print(f"You arrive at {location.location_description}")
                    location.discovered = True
                # For discovered locations (You return to...)
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

                # Options for movement.
                print(f"\nTo the North {Location.locations[location.north].cardinal_description}")
                print(f"To the East {Location.locations[location.east].cardinal_description}")
                print(f"To the South {Location.locations[location.south].cardinal_description}")
                print(f"To the West {Location.locations[location.west].cardinal_description}")

                # Input
                while not move:
                    player_input = input("What do you want to do? ").strip().upper().split(" ", 1)
                    action = player_input[0]
                    subject = player_input[1]

                    # If the player wants to inspect something.
                    if action == "INSPECT":
                        # Is the subject an item?
                        if subject in [item.name for item in Item.items]:
                            # Is the subject located in the current location?
                            if subject in [item.name for item in Location.locations[current_location_index].items]:
                                # Find the item.
                                for item in Location.locations[current_location_index].items:
                                    if item.name == subject:
                                        # Inspect it.
                                        item.inspect()
                                        # If it reveals another item.
                                        if isinstance(item, Reveals):
                                            new_item = item.reveals
                                            new_item.is_visible = True
                                            new_item.discovered = True
                            # Is the subject located in the players bag?
                            elif subject in [item.name for item in backpack.items()]:
                                # Find the item.
                                for item in backpack.items():
                                    if item.name == subject:
                                        # Inspect it.
                                        item.inspect()
                            else:
                                print(f"{subject} isn't located here or in your bag.")
                        else:
                            print(f"{subject} is not a valid item to INSPECT.")

                    # If the player wants to interact with something.
                    if action == "INTERACT":
                        # Insert something to be able to turn the key chamber in the dashboard.
                        if subject == "DASHBOARD":
                            # Boat key in bag.
                            if backpack.in_backpack(boat_key) >= 0:
                                print(f"{boat_key.name} inserted!\n{dashboard.key_true}")
                                dashboard.key = True
                                # Removes key from the game.
                                backpack.remove(boat_key, current_location)
                                current_location.dropped_items.remove(boat_key)
                            # Tension rod and key rake in bag.
                            elif backpack.in_backpack(tension_rod) >= 0 and backpack.in_backpack(key_rake) >= 0:
                                print(f"{tension_rod.name} applies the force!\n"
                                      f"{key_rake.name} depresses the pins!\n"
                                      f"{dashboard.key_true}")
                                dashboard.key = True
                                # Removes tension rod and key rake from the game.
                                backpack.remove(tension_rod, current_location)
                                backpack.remove(key_rake, current_location)
                                current_location.dropped_items.remove(tension_rod)
                                current_location.dropped_items.remove(key_rake)
                            # If the player doesn't have the required items.
                            else:
                                print("You don't have any way to turn the key in your bag...")

                        if subject == "COMPARTMENT":
                            if backpack.in_backpack(battery) >= 0:
                                print(f"{battery.name} inserted!\n{compartment.battery_true}")
                                compartment.battery = True
                                dashboard.power = True
                                # Removes key from the game.
                                backpack.remove(battery, current_location)
                                current_location.dropped_items.remove(battery)
                            if backpack.in_backpack(cable) >= 0:
                                compartment.cable = True
                                print(f"{cable.name} plugged in!")
                                if metal_box.insert:
                                    dashboard.power = True
                                    print(dashboard.power_true)
                                    # Removes cable from the game.
                                    backpack.remove(cable, current_location)
                                    current_location.dropped_items.remove(cable)
                                else:
                                    print(f"Now to find somewhere to plug other other end...")

                        if subject == "FUEL TANK":
                            if backpack.in_backpack(jerry) >= 0:
                                dashboard.fuel = True
                                fuel_tank.insert = True
                                print(f"{jerry.name} emptied into the fuel tank!")
                                fuel_tank.inspect()
                                backpack.remove(jerry, current_location)
                                current_location.dropped_items.remove(jerry)
                            if backpack.in_backpack(alcohol) >= 0:
                                dashboard.fuel = True
                                fuel_tank.insert = True
                                print(f"{alcohol.name} emptied into the fuel tank!")
                                fuel_tank.inspect()
                                backpack.remove(alcohol, current_location)
                                current_location.dropped_items.remove(alcohol)

                        if subject == "METAL BOX":
                            if backpack.in_backpack(cable) >= 0:
                                metal_box.insert = True
                                print(f"{cable.name} plugged in!")
                                if compartment.cable:
                                    dashboard.power = True
                                    # Removes cable from the game.
                                    backpack.remove(cable, current_location)
                                    current_location.dropped_items.remove(cable)
                                else:
                                    print(f"Now to find somewhere to plug other other end...")

                        if subject == "HANGING COCONUT":
                            if current_location_index == 2:
                                if coconut_item.is_visible:
                                    if backpack.rock:
                                        coconut_consumable.is_visible = True
                                        print("A perfect hit.")
                                        coconut_consumable.inspect()
                                        backpack.rock = False
                                    else:
                                        print("The COCONUT is out of reach.\nYou need something to throw at them...")
                                else:
                                    print("Hmm, maybe I should see if there are any in the PALM...")
                            else:
                                print("I think your in the wrong place for that...")

                        if subject == "SAND":
                            if backpack.in_backpack(shovel) >= 0:
                                sand.condition_met = True
                                print(sand.reveal_text)
                                new_item = sand.reveals
                                new_item.is_visible = True
                                new_item.discovered = True
                                # Removes shovel from the game.
                                backpack.remove(shovel, current_location)
                                current_location.dropped_items.remove(shovel)
                            else:
                                print("The sharp shells cut your hands.\nYou need something to dig with...")

                        if subject == "WATER":
                            if backpack.in_backpack(water_bottle) >= 0:
                                if water_bottle.is_full:
                                    print("The water bottle is already full")
                                else:
                                    water_bottle.is_full = True
                                    print("You fill up your water bottle.")

                    # To complete later
                    if action == "OPEN":
                        if subject == "BAG":
                            print(f"Your BAG currently had {backpack.count()} items.")
                            backpack.list()
                        else:
                            for item in Item.items:
                                if subject == item.name:
                                    try:
                                        item.Open()
                                    except:
                                        print(f"{item.name} cannot be opened.")

                    # To complete later
                    if action == "CLOSE":
                        for item in Item.items:
                            if subject == item.name:
                                item.Close()

                    # If the player wants to take something and put it in their bag.
                    if action == "TAKE":
                        # Is the subject an item that can be taken?
                        if subject in [item.name for item in Movable.movable_items] or subject == "Rock":
                            # Is the subject located in the current location?
                            if subject in [item.name for item in current_location.items]:
                                # Find the item.
                                for item in current_location.items:
                                    if item.name == subject:
                                        # If item is visible.
                                        if item.is_visible:
                                            # If getting the item has a condition.
                                            if isinstance(item, Conditional):
                                                if item.condition_met:
                                                    # Add it to your bag.
                                                    print(f"{item.name} added to your BAG.")
                                                    backpack.add(item)
                                                    # Remove it from the location.
                                                    Location.locations[current_location_index].items.remove(item)
                                                    # If it was revealed by another item.
                                                    if isinstance(item, RevealedMovable):
                                                        taken_from = item.revealed_by
                                                        taken_from.taken = True
                                                else:
                                                    # New text against what happens
                                                    pass
                                            elif item.name == "ROCK":
                                                if backpack.rock:
                                                    print("You already have a ROCK in your bag")
                                                else:
                                                    backpack.rock = True
                                            elif item.name == "COCONUT":
                                                if backpack.coconut:
                                                    print("You already have a COCONUT in your bag")
                                                else:
                                                    backpack.coconut = True
                                                    coconut_consumable.is_visible = False
                                            # Take the item.
                                            else:
                                                # Add it to your bag.
                                                print(f"{item.name} added to your BAG.")
                                                backpack.add(item)
                                                # Remove it from the location.
                                                Location.locations[current_location_index].items.remove(item)
                                                # If it was revealed by another item.
                                                if isinstance(item, RevealedMovable):
                                                    taken_from = item.revealed_by
                                                    taken_from.taken = True
                                                break
                                        else:
                                            print(f"{subject} can't be seem yet...")
                                            break
                            elif subject == "ROCK":
                                print(f"You can't seem to find any good {subject} here.")
                            else:
                                print(f"{subject} isn't located here.")
                        else:
                            print(f"{subject} is not a valid item to TAKE.")

                    # If the player wants to drop something from their bag.
                    if action == "DROP":
                        # Is the subject an item in their bag.
                        if subject in [item.name for item in backpack.items()]:
                            # Find the item.
                            for item in backpack.items():
                                if item.name == subject:
                                    # Remove it and drop it in the current location.
                                    backpack.remove(item, Location.locations[current_location_index])

                    if action == "PRESS" and subject == "BUTTON":
                        if current_location_index == button.location:
                            button.pressed()
                        else:
                            print("There is no button here.")

                    # If the player wants to move to another location.
                    if action == "MOVE":
                        # To move to the location to the North.
                        if subject == "N":
                            # If North goes into the sea.
                            if type(Location.locations[location.north]) is SeaLocation:
                                print(Location.locations[location.north].location_description)
                                exit()
                            # If North goes to an explorable location.
                            else:
                                current_location_index = location.north
                                move = True

                        # To move to the location to the East.
                        elif subject == "E":
                            # If East goes into the sea.
                            if type(Location.locations[location.east]) is SeaLocation:
                                print(Location.locations[location.east].location_description)
                                exit()
                            # If East goes to an explorable location.
                            else:
                                current_location_index = location.east
                                move = True

                        # To move to the location to the South.
                        elif subject == "S":
                            # If South goes into the sea.
                            if type(Location.locations[location.south]) is SeaLocation:
                                print(Location.locations[location.south].location_description)
                                exit()
                            # If South goes to an explorable location.
                            else:
                                current_location_index = location.south
                                move = True

                        # To move to the location to the West.
                        elif subject == "W":
                            # If West goes into the sea.
                            if type(Location.locations[location.west]) is SeaLocation:
                                print(Location.locations[location.west].location_description)
                                exit()
                            # If West goes to an explorable location.
                            else:
                                current_location_index = location.west
                                move = True

                        else:
                            print(f"The input {subject} is not a valid direction.\nMOVE (N, E, S, W)")

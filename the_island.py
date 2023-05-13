import time
from os import system, name
from game.locations.location_zero import *
from game.locations.location_one import *
from game.locations.location_two import *
from game.locations.location_three import *
from game.locations.location_four import *
from game.locations.location_five import *
from game.locations.location_six import *
from game.locations.location_seven import *
from game.locations.location_eight import *
from game.locations.location_nine import *
from game.locations.location_ten import *
from game.locations.locations_surrounding import *


def typing(string):
    """
    Prints a string letter by letter to simulate typing.
    :param string: The string to print letter by letter
    """
    for letter in string:
        print(letter, end='', flush=True)
        time.sleep(0.01)
    time.sleep(0.5)
    print("")


def clear_screen():
    """
    When used in the terminal, will clear everything from the screen.
    """
    # for Windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux (here os.name is 'posix')
    else:
        _ = system('clear')
    print()


def load_location_items(load_location):
    """
    Prints a complete description for the locations items, current energy and hydration levels, and surroundings.
    :param load_location: The location that is being loaded.
    """
    # Display all static items
    for location_item in load_location.get_location_items():
        if location_item.get_visibility_status() and not isinstance(location_item, Movable):
            location_item.item_discovered()
            print(location_item.get_location_description_text())
        # Display movable items that haven't been moved.
        elif location_item.get_visibility_status() and isinstance(location_item, Movable) \
                and not location_item.get_moved_status():
            location_item._discovery_status = True
            print(location_item.get_location_description_text())
        # Display movable items that have been moved and dropped in a location.
        elif location_item.get_visibility_status() and isinstance(location_item, Movable) \
                and location_item.get_moved_status():
            print(f"On the ground lies the dropped {location_item.get_name()}")
    # Display current energy and hydration levels.
    print(f"\nYou currently have enough energy for {energy} moves.")
    print(f"You currently have enough hydration for {hydration} moves")
    # Options for movement.
    print(f"\nTo the NORTH (N) {Location.locations[location.get_north_id()].get_cardinal_description_text()}")
    print(f"To the EAST (E) {Location.locations[location.get_east_id()].get_cardinal_description_text()}")
    print(f"To the SOUTH (S) {Location.locations[location.get_south_id()].get_cardinal_description_text()}")
    print(f"To the WEST (W) {Location.locations[location.get_west_id()].get_cardinal_description_text()}")


if __name__ == '__main__':
    # Keep track of objectives.
    boat_end = False
    kraken_block_attempts = 0
    kraken_end = False
    ocean_death_end = False
    land_death_end = False

    # Keep track of player.
    ability = None
    moves = 0
    energy = 10
    hydration = 10

    # Reset Chart
    chart.reset_chart(Location.locations)

    # Keep track of the current location.
    current_location_index = 0
    current_location = Location.locations[current_location_index]

    # Load all the items into their respective locations.
    for location in ExplorableLocation.locations:
        for item in Item.items:
            if item.get_initial_location_id() == location.get_location_id():
                location.add_item_to_location(item)

    # Start
    clear_screen()
    typing("'Any callsign. This is Coastguard. Are you receiving. Over'")
    time.sleep(1)
    typing("'Any callsign. Any callsign'")
    typing("'This is. This is'")
    typing("'Coastguard. Coastguard'")
    typing("'Are you receiving. Are you receiving'")
    typing("'Over'\n")
    time.sleep(1)
    print("You open your eyes, the bright sun blinds you for a moment.")
    print("You grab the radio.\n")
    time.sleep(1)
    typing("'Coastguard. This is...'")
    time.sleep(1)
    player_name = ""
    while player_name == "":
        print("Who am I again?")
        player_name = input("- ").capitalize().strip()
    clear_screen()
    time.sleep(1)
    typing(f"'Coastguard. This is {player_name}. Receiving. Over'")
    typing(f"'Coastguard. Glad we found you {player_name}. We have been looking for you for days. Break'")
    typing("'We can't make it to The Island, you're going to have to get to us. Break'")
    typing("'We're anchored twenty nautical miles to the South. Over'")
    typing(f"'{player_name}. Acknowledged. I will let you know when I'm on the way. Over'")
    typing("'Coastguard. Roger. If you need any further instructions on what to do. Break'")
    typing("'Simply type 'HELP' and press [ENTER] to call us. Out'")
    print("\nPress [ENTER] to continue.")
    input("- ")

    clear_screen()
    print("More memories coming flooding back. I remember I was good at something...")
    time.sleep(1)
    print("\nStrength: You have the strength of an Ox, you can carry 10 items in your backpack instead of 5.")
    print("Dexterity: You are light on your feet, moving only takes energy and hydration every second turn.")
    print("Charisma: You speak well and seem to be liked naturally, other want to help you more.")
    print("Intelligence: You just seem to know more, food and drink items now have statistics.")

    while True:
        print("\nWhat was it again? (Strength / Dexterity / Charisma / Intelligence)")
        ability = input("- ").strip().upper()
        if ability == "STRENGTH":
            backpack.set_capacity(10)
            break
        if ability == "DEXTERITY":
            break
        if ability == "CHARISMA":
            kraken_block_attempts = -2
            break
        if ability == "INTELLIGENCE":
            break

    print(f"Ah yes, I have elite levels of {ability.lower()}.")
    time.sleep(1)

    print("\nPress [ENTER] to begin your adventure on The Island.")
    input("- ")
    while boat_end is False and kraken_end is False and ocean_death_end is False and land_death_end is False:
        # Get the current location information.
        for location in Location.locations:
            if location.get_location_id() == current_location_index:
                # Set or reset move to false.
                move = False
                clear_screen()
                # Mark location as discovered on chart.
                if not current_location.get_discovery_status():
                    chart.location_discovered(current_location)
                else:
                    chart.add_player_location(current_location)

                # Starting text for first location the first time.
                if moves == 0:
                    print(f"You look around and realise you're on {location.get_start_text()}")
                    print(f"You have a Bag (B), which can hold {backpack.get_capacity()} items.")
                    print(f"You also have a Chart (C) of The Island.")
                    location.location_discovered()
                # Once the player starts moving.
                else:
                    # For undiscovered locations (You arrive at...).
                    if not location.get_discovery_status():
                        print(f"You arrive at {location.get_location_description_text()}")
                        location.location_discovered()
                    # For discovered locations (You return to...).
                    else:
                        print(f"You return to {location.get_location_description_text()}")

                # Print in all the items and options for the location.
                load_location_items(current_location)

                # Creates a loop for actions until the player moves.
                while not move:
                    # Ask the player what they want to do.
                    print("\nWhat do you want to do now?")
                    print("Help (H) / Refresh (R) / Bag (B) / Chart (C)")
                    print("Look (L) / Move (M) / Interact (I) / Open (O) / Take (T) / Drop (D) / Speak (S) / "
                          "Eat (E) + CAPITALIZED NOUN")
                    player_input = input("- ").strip().upper().split(" ", 1)
                    print("")
                    # If the player didn't enter anything.
                    if player_input[0] == "":
                        print("You did not enter anything.")
                    # If the player entered one word.
                    elif len(player_input) == 1:

                        # The player needs help.
                        if player_input[0] == "HELP" or player_input[0] == "H":
                            # Contact helper.
                            typing(f"'Coastguard. This is {player_name}. Are you receiving. Over'")
                            typing(f"'{player_name}. This is Coastguard. Receiving. How can we help. Over'")
                            # Create a loop while the player still needs help.
                            while True:
                                # Input what they need help with.
                                print("What would you like help with? (Basics / Goals / Actions / Nothing)")
                                response = input("- ").upper().strip()
                                typing(f"'{player_name}. {response}. Over'")
                                # Need help with the basics of the game.
                                if response == "BASICS":
                                    # Basics of the game.
                                    typing("'Coastguard. You are currently on The Island. Break'")
                                    typing("'Anything that is of importance will be written in 'CAPITALS'. Break'")
                                    typing("'Do not wander into the water, it's too dangerous. Break'")
                                    typing("'You can move around The Island to explore different areas. Break'")
                                    typing("'Remember to eat and drink. Don't want you dying on us. Break'")
                                    typing("'You need to get to us, we're 20 nautical miles to the South. Break'")
                                    typing("'Can we help you with anything else. Over'")
                                # Need help with the goals of the game.
                                elif response == "GOALS":
                                    # Goal
                                    typing("'Coastguard. You need to get to us. Break'")
                                    typing("'Find a boat, get it working or by any other means you can. Break'")
                                    typing("'Can we help you with anything else. Over'")
                                # Need help with action within the game.
                                elif response == "ACTIONS":
                                    # Basic actions.
                                    typing("'Coastguard. You can use the following actions on The Island. Break'")
                                    typing("'Help (H) / Refresh (R) / Bag (B) / Chart (C). Break'")
                                    typing("'These do not require any noun to work with. Break'")
                                    typing("'Look (L) / Move (M) / Interact (I) / Open (O) / Take (T) / Drop (D) / "
                                           "Speak (S) / Eat (E). Break''")
                                    typing("'These require a CAPITALIZED NOUN to work with. Break'")
                                    typing("'Shorthand also works, with just the first letter of the action. Break'")
                                    typing("'So instead of 'Look' + Noun, use 'L' + Noun. Break'")
                                    typing("'Simply type what you want to do followed by the [ENTER] key. Break'")
                                    typing("'Do you require more information on any of these. Over'")
                                    # Create a loop while the player still needs help with actions.
                                    while True:
                                        # Input what action they need help with.
                                        print("(Refresh / Help / Bag / Chart / Look / Move / Interact / Open / Take / "
                                              "Drop / Speak / Eat / No)")
                                        response = input("- ").upper().strip()
                                        typing(f"'{player_name}. {response}. Over'")
                                        # Help action.
                                        if response == "HELP":
                                            typing("'Coastguard. This will get you in touch with us again. Break")
                                            typing("'We are here whenever you need us. Break")
                                            typing("'Do you need more information on any others. Over")
                                        # Refresh action.
                                        elif response == "REFRESH":
                                            typing("'Coastguard. Sometimes there is too much information. Break'")
                                            typing("'Or the screen may become crowded, making you lose track. Break'")
                                            typing("'This will reprint all the information for the location. Break'")
                                            typing("'Do you need more information on any others. Over'")
                                        # Bag action.
                                        elif response == "BAG":
                                            typing("'Coastguard. You should have a bag with you. Break'")
                                            typing("'When you take an item, it will be placed in your bag. Break'")
                                            typing("'You can use this command to see what's in your bag. Break'")
                                            typing("'Do you need more information on any others. Over'")
                                        # Chart action.
                                        elif response == "CHART":
                                            typing("'Coastguard. You should have a chart with you. Break'")
                                            typing("'It will give you an overview of The Island. Break'")
                                            typing("'It will keep track of places you've been. Break'")
                                            typing("'Do you need more information on any others. Over'")
                                        # Look action.
                                        elif response == "LOOK":
                                            typing("'Coastguard. This gives you information about an item. Break")
                                            typing("'It may reveal more items. Break")
                                            typing("'It needs a subject ie. Look Pole / L Pole. Break")
                                            typing("'Do you need more information on any others. Over")
                                        # Move action
                                        elif response == "MOVE":
                                            typing("'Coastguard. Your going to have to move around. Break'")
                                            typing("'Use cardinal directions to go in that direction. Break'")
                                            typing("'It needs a subject ie. Move North / M North. Break'")
                                            typing("'You can shorthand the direction too ie. M N. Break'")
                                            typing("'Do you need more information on any others. Over'")
                                        # Interact action.
                                        elif response == "INTERACT":
                                            typing("'Coastguard. If you have an item in you bag. Break")
                                            typing("'And you think you can use it with another item. Break'")
                                            typing("'Or you need to enter a code or something. Break")
                                            typing("'It needs a subject ie. Interact Ball / I Ball. Break")
                                            typing("'And will only work if you have the bat in your bag. Break")
                                            typing("'Do you need more information on any others. Over")
                                        # Open action
                                        elif response == "OPEN":
                                            typing("'Coastguard. Sometimes things will be closed. Break'")
                                            typing("'You can open them with this, if they aren't locked. Break'")
                                            typing("'It needs a subject ie. Open Door / O Door. Break'")
                                            typing("'Do you need more information on any others. Over'")
                                        # Take action
                                        elif response == "TAKE":
                                            typing("'Coastguard. There are many movable things on The Island. Break'")
                                            typing("'You can pick them up to put in your bag. Break'")
                                            typing("'It needs a subject ie. Take Hat / T Hat. Break'")
                                            typing("'Do you need more information on any others. Over'")
                                        # Drop action
                                        elif response == "DROP":
                                            typing("'Coastguard. If you need to make room in your bag. Break'")
                                            typing("'Drop a item. It will remain there if you want it again. Break'")
                                            typing("'It needs a subject ie. Drop Hat / D Hat. Break'")
                                            typing("'Do you need more information on any others. Over'")
                                        # Talk action
                                        elif response == "SPEAK":
                                            typing("'Coastguard. I hear there are other being on The Island. Break'")
                                            typing("'They may be able to help you, so talk to them. Break'")
                                            typing("'It needs a subject ie. Speak Pirate / S Pirate. Break'")
                                            typing("'Do you need more information on any others. Over'")
                                        # Consume action
                                        elif response == "EAT":
                                            typing("'Coastguard. You lose energy and hydration as you move. Break'")
                                            typing("'Eat and drink edible items to replenish this . Break'")
                                            typing("'It needs a subject ie. Eat Apple / E Apple. Break'")
                                            typing("'Do you need more information on any others. Over'")
                                        # None to break the help for actions.
                                        elif response == "NO":
                                            typing("'Coastguard. Roger. Anything else I can help you with. Over'")
                                            break
                                        # Any other response.
                                        else:
                                            # Invalid
                                            typing(f"'Coastguard. You are broken and unreadable. Say again. Over'")
                                # No longer require help.
                                elif response == "NOTHING":
                                    # Break help loop
                                    typing(f"'Coastguard. Roger. Out'")
                                    break
                                # Did not enter a valid response.
                                else:
                                    # Invalid response.
                                    typing(f"'Coastguard. You are broken and unreadable. Say again. Over'")

                        # The player wants the items and choices rewritten.
                        if player_input[0] == "REFRESH" or player_input[0] == "R":
                            # Reloads and prints all choices for the location.
                            clear_screen()
                            load_location_items(current_location)

                        # If the player wants to open their bag .
                        elif player_input[0] == "BAG" or player_input[0] == "B":
                            # Print bag inventory
                            print(backpack.list())

                        # If the player wants to open their chart.
                        elif player_input[0] == "CHART" or player_input[0] == "C":
                            # Open chart.
                            print(chart.show_chart())

                        # Any other one word input.
                        else:
                            print(f"{player_input[0]} is not a valid one word action.\n")

                    # If the player entered more than one word.
                    elif len(player_input) >= 1:
                        # Split into the action they want to do.
                        action = player_input[0]
                        # And the noun to do it upon.
                        noun = player_input[1]

                        # If the player wants to inspect something.
                        if action == "LOOK" or action == "L":
                            # Is the noun an item?
                            if noun in [item.get_name() for item in Item.items]:
                                # Is the noun located in the current location?
                                if noun in [item.get_name() for item in current_location.get_location_items()]:
                                    # Find the item.
                                    for item in current_location.get_location_items():
                                        if item.get_name() == noun:
                                            # Is visible.
                                            if item.get_visibility_status():
                                                if isinstance(item, Consumable):
                                                    if ability == "INTELLIGENCE":
                                                        print(item.intelligent_inspect())
                                                    else:
                                                        print(item.inspect())
                                                else:
                                                    print(item.inspect())
                                            # Not visible yet.
                                            else:
                                                print(f"{noun} can't be seen in this location yet.")
                                # Is the noun located in the players bag?
                                elif noun in [item.get_name() for item in backpack.items()]:
                                    # Find the item.
                                    for item in backpack.items():
                                        if item.get_name() == noun:
                                            # Inspect it.
                                            print(item.inspect())
                                # The noun isn't located in the current location or the players bag.
                                else:
                                    print(f"{noun} isn't located here or in your bag.")
                            # The noun isn't a valid item to inspect.
                            else:
                                print(f"{noun} is not a valid item to {action}.")

                        # If the player wants to move to another location.
                        elif action == "MOVE" or action == "M":
                            # To move to the location to the North.
                            if noun == "NORTH" or noun == "N":
                                # Movement is true and add one to move tally.
                                move = True
                                moves += 1
                                # If North goes to sea location and death.
                                if type(Location.locations[location.get_north_id()]) is SeaLocation:
                                    while True:
                                        print(f"Please confirm the move, as "
                                              f"{Location.locations[location.get_north_id()].get_cardinal_description_text()} "
                                              f"(Yes / No)")
                                        confirm = input("- ").strip().upper()
                                        if confirm == "YES":
                                            clear_screen()
                                            print(Location.locations[location.get_north_id()].
                                                  get_location_description_text())
                                            ocean_death_end = True
                                            break
                                        elif confirm == "NO":
                                            break
                                        else:
                                            print("\nYou must confirm either Yes or No.")
                                # If North goes to an explorable location.
                                else:
                                    chart.remove_player_location(current_location)
                                    current_location_index = location.get_north_id()
                                    current_location = Location.locations[current_location_index]

                            # To move to the location to the East.
                            elif noun == "EAST" or noun == "E":
                                # Movement is true and add one to move tally.
                                move = True
                                moves += 1
                                # If East goes to sea location and death.
                                if type(Location.locations[location.get_east_id()]) is SeaLocation:
                                    while True:
                                        print(f"Please confirm the move, as "
                                              f"{Location.locations[location.get_east_id()].get_cardinal_description_text()} "
                                              f"(Yes / No)")
                                        confirm = input("- ").strip().upper()
                                        if confirm == "YES":
                                            clear_screen()
                                            print(Location.locations[location.get_east_id()].
                                                  get_location_description_text())
                                            ocean_death_end = True
                                            break
                                        elif confirm == "NO":
                                            break
                                        else:
                                            print("\nYou must confirm either Yes or No.")

                                # If East goes to an explorable location.
                                else:
                                    chart.remove_player_location(current_location)
                                    current_location_index = location.get_east_id()
                                    current_location = Location.locations[current_location_index]

                            # To move to the location to the South.
                            elif noun == "SOUTH" or noun == "S":
                                # Movement is true and add one to move tally.
                                move = True
                                moves += 1
                                # If South goes to sea location and death.
                                if type(Location.locations[location.get_south_id()]) is SeaLocation:
                                    while True:
                                        print(f"Please confirm the move, as "
                                              f"{Location.locations[location.get_south_id()].get_cardinal_description_text()} "
                                              f"(Yes / No)")
                                        confirm = input("- ").strip().upper()
                                        if confirm == "YES":
                                            clear_screen()
                                            print(Location.locations[location.get_south_id()].
                                                  get_location_description_text())
                                            ocean_death_end = True
                                            break
                                        elif confirm == "NO":
                                            break
                                        else:
                                            print("\nYou must confirm either Yes or No.")

                                # If South goes to an explorable location.
                                else:
                                    chart.remove_player_location(current_location)
                                    current_location_index = location.get_south_id()
                                    current_location = Location.locations[current_location_index]

                            # To move to the location to the West.
                            elif noun == "WEST" or noun == "W":
                                # Movement is true and add one to move tally.
                                move = True
                                moves += 1
                                # If West goes to sea location and death.
                                if type(Location.locations[location.get_west_id()]) is SeaLocation:
                                    while True:
                                        print(f"Please confirm the move, as "
                                              f"{Location.locations[location.get_west_id()].get_cardinal_description_text()} "
                                              f"(Yes / No)")
                                        confirm = input("- ").strip().upper()
                                        if confirm == "YES":
                                            clear_screen()
                                            print(Location.locations[location.get_west_id()].
                                                  get_location_description_text())
                                            ocean_death_end = True
                                            break
                                        elif confirm == "NO":
                                            break
                                        else:
                                            print("\nYou must confirm either Yes or No.")

                                # If West goes to an explorable location.
                                else:
                                    chart.remove_player_location(current_location)
                                    current_location_index = location.get_west_id()
                                    current_location = Location.locations[current_location_index]

                            # Invalid noun with action MOVE.
                            else:
                                print(f"The input {noun} is not a valid direction.\n"
                                      f"If you want to move, "
                                      f"please choose on of the following (North / East / South / West)")
                                continue

                            # Minus energy and hydration.
                            if ability == "DEXTERITY":
                                if moves % 2 == 0:
                                    energy -= 1
                                    hydration -= 1
                            else:
                                energy -= 1
                                hydration -= 1

                            # Allow time to ready final text.
                            if ocean_death_end:
                                print("\nPress [ENTER] to continue.")
                                input("- ")

                        # If the player wants to interact with something.
                        elif action == "INTERACT" or action == "I":
                            # Insert something to be able to turn the key chamber in the dashboard.
                            if noun == "DASHBOARD":
                                # Is the noun here?
                                if dashboard in current_location.get_location_items():
                                    # Do you have the required item?
                                    if boat_key in backpack.items():
                                        print(f"{boat_key.get_name()} inserted!\n{dashboard.get_key_true_text()}")
                                        dashboard.key_inserted()
                                        # Removes item from the game.
                                        print(backpack.remove(boat_key, current_location))
                                        current_location.remove_location_item(boat_key)
                                    # Do you have the required items?
                                    elif tension_rod in backpack.items() and key_rake in backpack.items():
                                        print(f"{tension_rod.get_name()} applies the force!\n"
                                              f"{key_rake.get_name()} depresses the pins!\n"
                                              f"{dashboard.get_key_true_text()}")
                                        dashboard.key_inserted()
                                        # Removes items from the game.
                                        backpack.remove(tension_rod, current_location)
                                        backpack.remove(key_rake, current_location)
                                        current_location.remove_location_item(key_rake)
                                        current_location.remove_location_item(tension_rod)
                                    # Doesn't have the required item.
                                    else:
                                        print("I don't have any way to turn the key chamber in my bag...")
                                # Wrong location.
                                else:
                                    # Invalid
                                    print(f"The is no {noun} here.")

                            # Insert something into the compartment to power the boat.
                            elif noun == "COMPARTMENT":
                                # Is the noun here?
                                if compartment in current_location.get_location_items():
                                    # Do you have the required item?
                                    if battery in backpack.items():
                                        print(f"{battery.get_name()} inserted!\n"
                                              f"{compartment.get_battery_true_text()}")
                                        compartment.battery_inserted()
                                        dashboard.dashboard_powered()
                                        # Removes item from the game.
                                        backpack.remove(battery, current_location)
                                        current_location.remove_location_item(battery)
                                    # Do you have the required item?
                                    elif cable in backpack.items():
                                        compartment.cable_inserted()
                                        print(f"{cable.get_name()} plugged in!\n"
                                              f"{compartment.get_cable_true_text()}")
                                        # If the cable is plugged into the metal box.
                                        if metal_box.get_insert_status():
                                            dashboard.dashboard_powered()
                                            # Removes item from the game.
                                            backpack.remove(cable, current_location)
                                            current_location.remove_location_item(cable)
                                        # Hint they need to do that.
                                        else:
                                            print(f"Now to find somewhere to plug other other end...")
                                    # Doesn't have the required item.
                                    else:
                                        print("I have any way to supply power in my bag...")
                                # Wrong location.
                                else:
                                    print(f"The is no {noun} here.")

                            # Insert something into the fuel tank to fuel the boat.
                            elif noun == "FUEL TANK":
                                # Is the noun here?
                                if fuel_tank in current_location.get_location_items():
                                    # Do you have the required item?
                                    if jerry in backpack.items():
                                        dashboard.boat_fueled()
                                        fuel_tank.item_inserted()
                                        print(f"{jerry.get_name()} emptied into the fuel tank.\n"
                                              f"{fuel_tank.get_full_text()}")
                                        # Removes item from the game.
                                        print(backpack.remove(jerry, current_location))
                                        current_location.remove_location_item(jerry)
                                    # Do you have the required item?
                                    elif alcohol in backpack.items():
                                        dashboard.boat_fueled()
                                        fuel_tank.item_inserted()
                                        print(f"{alcohol.get_name()} emptied into the fuel tank.\n"
                                              f"{fuel_tank.get_full_text()}")
                                        # Removes item from the game.
                                        print(backpack.remove(alcohol, current_location))
                                        current_location.remove_location_item(alcohol)
                                    # Doesn't have the required item.
                                    else:
                                        print(f"I need something to fill the tank with...")
                                # Wrong location.
                                else:
                                    print(f"The is no {noun} here.")

                            # Insert something into the metal box to help power the boat.
                            elif noun == "METAL BOX":
                                # Is the noun here?
                                if metal_box in current_location.get_location_items():
                                    # Do you have the required item?
                                    if cable in backpack.items():
                                        metal_box.item_inserted()
                                        print(f"{cable.get_name()} plugged in.\n{metal_box.get_full_text()}")
                                        # If the cable is plugged in at the other end.
                                        if compartment.get_cable_status():
                                            dashboard.dashboard_powered()
                                            # Removes item from the game.
                                            backpack.remove(cable, current_location)
                                            current_location.remove_location_item(cable)
                                        # Hint to find other place to plug in
                                        else:
                                            print(f"Now to find somewhere to plug in other other end...")
                                    # Doesn't have the required item.
                                    else:
                                        print(f"I need to find something to plug in here...")
                                # Wrong location.
                                else:
                                    print(f"The is no {noun} here.")

                            # Enter the pass code into the keypad.
                            elif noun == "KEYPAD":
                                # Is the noun here?
                                if keypad in current_location.get_location_items():
                                    # Is it visible?
                                    if keypad.get_visibility_status():
                                        print("Please enter the 4 digit code.")
                                        input_code = input("- ").upper().strip()
                                        if input_code == keypad.get_access_code():
                                            print(heavy_chest.unlock_container())
                                        else:
                                            print(f"{heavy_chest.get_name()} remains locked.")
                                    # Invalid.
                                    else:
                                        print(f"{noun} can't be seen in this location... yet.")
                                # Invalid.
                                else:
                                    print(f"The is no {noun} here.")

                            # Press the button to start the boat.
                            elif noun == "BUTTON":
                                if button in current_location.get_location_items():
                                    # All conditions met to start boat.
                                    if dashboard.get_key_status() and dashboard.get_power_status() \
                                            and dashboard.get_fuel_status():
                                        print("\nThe boat engine roars to life as you cast of the rope.")
                                        boat_end = True
                                        print("\nPress [ENTER] to continue.")
                                        input("- ")
                                        break
                                    else:
                                        print("Nothing happens...")
                                # Wrong location.
                                else:
                                    print(f"The is no {noun} here.")

                            # Throw a rock at the coconut.
                            elif noun == "COCONUT":
                                # Is the noun here?
                                if coconut in current_location.get_location_items():
                                    # Is it visible?
                                    if coconut.get_visibility_status():
                                        # Do you have the required item?
                                        if rock in backpack.items():
                                            print(f"A perfect hit.\n{coconut.get_coconut_ground_text()}")
                                            palm.item_one_taken()
                                            coconut.condition_met()
                                            coconut.set_location_description_text(coconut.get_coconut_ground_text())
                                            # Removes item from the game.
                                            backpack.remove(rock, current_location)
                                            current_location.remove_location_item(rock)
                                        # Hint
                                        else:
                                            print(
                                                "The COCONUT is out of reach.\n"
                                                "You need something to throw at it...")
                                    # Not visible.
                                    else:
                                        print(f"{noun} can't be seen in this location yet.")
                                # Wrong location.
                                else:
                                    print(f"The is no {noun} here.")

                            # Dig in the sand.
                            elif noun == "SAND":
                                # Is the noun here?
                                if sand in current_location.get_location_items():
                                    # Do you have the required item?
                                    if shovel in backpack.items():
                                        sand.condition_met()
                                        print("You begin to dig with your shovel...")
                                        time.sleep(1)
                                        print(f"What have we here.\n{sand.get_reveal_text()}")
                                        revealed_item = sand.get_revealed_item()
                                        revealed_item.make_visible()
                                        revealed_item.item_discovered()
                                        # Removes item from the game.
                                        backpack.remove(shovel, current_location)
                                        current_location.remove_location_item(shovel)
                                    # Hint
                                    else:
                                        print("The sharp shells cut your hands.\nYou need something to dig with...")
                                # Wrong location.
                                else:
                                    print(f"The is no {noun} here.")

                            # Insert numbered blocks into the block.
                            elif noun == "BLOCK":
                                # Is the noun here?
                                if block in current_location.get_location_items():

                                    # Get numbered blocks in bag.
                                    numbered_blocks = []
                                    numbered_blocks_string = ""
                                    for item in backpack.items():
                                        if item.get_name().startswith("BLOCK"):
                                            numbered_blocks.append(item)
                                    if len(numbered_blocks) == 0 and all(
                                            slot is None for slot in block.list_slot_items()):
                                        print("You don't have any granite blocks to insert.\n"
                                              "There are no granite blocks inserted for you to take.")
                                    else:
                                        for numbered_block in numbered_blocks:
                                            numbered_blocks_string += f"{numbered_block.get_name().split()[1]} / "

                                        # Get available and occupied slots.
                                        slots = block.list_slot_items()
                                        available_slots = []
                                        available_slots_string = ""
                                        occupied_slots = []
                                        occupied_slots_string = ""
                                        for i, slot in enumerate(slots, start=1):
                                            if slot is None:
                                                available_slots.append(str(i))
                                                available_slots_string += f"{str(i)} / "
                                            else:
                                                occupied_slots.append(str(i))
                                                occupied_slots_string += f"{str(i)} / "
                                        # Get interation options.
                                        interact_options_string = ""
                                        if len(numbered_blocks) > 0 and any(
                                                slot is not None for slot in block.list_slot_items()):
                                            interact_options_string = "Insert / Take / "
                                        elif len(numbered_blocks) > 0 and all(
                                                slot is None for slot in block.list_slot_items()):
                                            interact_options_string = "Insert / "
                                        elif len(numbered_blocks) == 0 and any(
                                                slot is not None for slot in block.list_slot_items()):
                                            interact_options_string = "Take / "
                                        else:
                                            pass
                                        # Initial options
                                        print(f"What would you like to do? "
                                              f"({interact_options_string}Leave)")
                                        action_choice = input("- ").upper().strip()
                                        # Insert
                                        if action_choice == "INSERT" and len(numbered_blocks) > 0:
                                            # Slot options
                                            print(f"\nInto which slot would you like to insert a block? "
                                                  f"({available_slots_string}Leave)")
                                            slot_choice = input("- ").upper().strip()
                                            # Valid.
                                            if slot_choice in available_slots:
                                                # Option to insert
                                                print(f"\nWhich block would you like to insert? "
                                                      f"({numbered_blocks_string}Leave)")
                                                numbered_block_choice = input("- ").upper().strip()
                                                # Valid.
                                                if numbered_block_choice in [numbered_block.get_name().split()[1] for
                                                                             numbered_block in numbered_blocks]:
                                                    for numbered_block in numbered_blocks:
                                                        if numbered_block_choice == numbered_block.get_name().split()[1]:
                                                            # Insert into slot 1.
                                                            if slot_choice == "1" and block.get_slot_one_item() is None:
                                                                print(
                                                                    f"\n{backpack.remove(numbered_block, current_location)}")
                                                                current_location.remove_location_item(numbered_block)
                                                                block.set_slot_one_item(numbered_block)
                                                                print(
                                                                    f"Slot 1 now contains {numbered_block.get_name()}")
                                                            # Insert into slot 2.
                                                            elif slot_choice == "2" and block.get_slot_two_item() is None:
                                                                print(
                                                                    f"\n{backpack.remove(numbered_block, current_location)}")
                                                                current_location.remove_location_item(numbered_block)
                                                                block.set_slot_two_item(numbered_block)
                                                                print(
                                                                    f"Slot 2 now contains {numbered_block.get_name()}")
                                                            # Insert into slot 3.
                                                            elif slot_choice == "3" and block.get_slot_three_item() is None:
                                                                print(
                                                                    f"\n{backpack.remove(numbered_block, current_location)}")
                                                                current_location.remove_location_item(numbered_block)
                                                                block.set_slot_three_item(numbered_block)
                                                                print(
                                                                    f"Slot 3 now contains {numbered_block.get_name()}")
                                                # Break loop.
                                                elif numbered_block_choice == "LEAVE":
                                                    pass
                                                # Invalid.
                                                else:
                                                    print(f"\nBlock {numbered_block_choice} is not in your bag.")
                                            # Break loop.
                                            elif slot_choice == "LEAVE":
                                                pass
                                            # Invalid.
                                            else:
                                                print(f"Slot {slot_choice} is not a valid option.")

                                            # After block insert
                                            # If three blocks inserted and correct.
                                            if block.get_slot_one_item() == block_six and \
                                                    block.get_slot_two_item() == block_zero and \
                                                    block.get_slot_three_item() == block_five:
                                                print("\nWell that's all the slots filled...")
                                                print(f"{block.get_slot_items()}")
                                                time.sleep(2)
                                                # Complete puzzle and game. Break loop.
                                                print("\nA giant tentacle pulls you forward and over the cliff.\n"
                                                      "It holds you just above the water..\n"
                                                      "In your head you hear a voice...\n"
                                                      "You have solved the puzzle, so shall help you.\n"
                                                      "I know where you need to go, I've been watching them too.\n"
                                                      "You move around The Island and to the South in the Krakens grasp.")
                                                kraken_end = True
                                                print("\nPress [ENTER] to continue.")
                                                input("- ")
                                                break
                                            # If three blocks inserted and incorrect.
                                            elif all(slot is not None for slot in block.list_slot_items()):
                                                # Still has attempts left.
                                                if kraken_block_attempts < 2:
                                                    kraken_block_attempts += 1
                                                    move = True
                                                    chart.remove_player_location(current_location)
                                                    current_location_index = location.get_south_id()
                                                    current_location = Location.locations[current_location_index]
                                                    print("\nWell that's all the slots filled...")
                                                    print(f"{block.get_slot_items()}")
                                                    time.sleep(2)
                                                    print("The water in front of you explodes")
                                                    print("I giant tentacle knocks you back onto the flat plain.")
                                                    loc_eight.add_item_to_location(block.get_slot_one_item())
                                                    loc_eight.add_item_to_location(block.get_slot_two_item())
                                                    loc_eight.add_item_to_location(block.get_slot_three_item())
                                                    block.set_slot_one_item(None)
                                                    block.set_slot_two_item(None)
                                                    block.set_slot_three_item(None)
                                                    print("The blocks you had previously inserted land around you.")
                                                    print("\nPress [ENTER] to continue.")
                                                    input("- ")
                                                    break
                                                # Too many attempts and lose game.
                                                else:
                                                    print("\nWell that's all the slots filled...")
                                                    print(f"{block.get_slot_items()}")
                                                    time.sleep(2)
                                                    print("The water in front of you explodes.\n"
                                                          "This time the giant tentacle pulls you forward.\n"
                                                          "You're plunged into the endless abyss below the cliff.\n"
                                                          "Descending fast, the light soon disappears.\n"
                                                          "You lose consciousness surrounded by darkness...")
                                                    ocean_death_end = True
                                                    print("\nPress [ENTER] to continue.")
                                                    input("- ")
                                                    break
                                        # Take
                                        elif action_choice == "TAKE" and any(
                                                slot is not None for slot in block.list_slot_items()):
                                            # Slot option
                                            print(f"\n{block.get_slot_items()}")
                                            print(f"Which slot do you want to take a BLOCK from? "
                                                  f"({occupied_slots_string}Leave)")
                                            take_choice = input("- ").upper().strip()
                                            # From slot 1.
                                            if take_choice == "1" and block.get_slot_one_item() is not None:
                                                print(f"\n{backpack.add(block.get_slot_one_item())}")
                                                block.set_slot_one_item(None)
                                                print(f"Slot 1 is now empty")
                                            # From slot 2.
                                            elif take_choice == "2" and block.get_slot_two_item() is not None:
                                                print(f"\n{backpack.add(block.get_slot_two_item())}")
                                                block.set_slot_two_item(None)
                                                print(f"Slot 2 is now empty")
                                            # From slot 3.
                                            elif take_choice == "3" and block.get_slot_three_item() is not None:
                                                print(f"\n{backpack.add(block.get_slot_three_item())}")
                                                block.set_slot_three_item(None)
                                                print(f"Slot 3 is now empty")
                                            # Break loop
                                            elif take_choice == "LEAVE":
                                                pass
                                            # Invalid.
                                            else:
                                                print(f"\nSlot {take_choice} is not a valid option.")
                                        # Break loop
                                        elif action_choice == "LEAVE":
                                            pass
                                        # Invalid
                                        else:
                                            print(f"\n{action_choice} isn't a valid choice.")

                                # Wrong location.
                                else:
                                    print(f"The is no {noun} here.")

                            else:
                                print(f"{noun} is not a valid item to {action} with.")

                        # If the player wants to open something.
                        elif action == "OPEN" or action == "O":
                            # Is the noun an item.
                            if noun in [item.get_name() for item in Item.items]:
                                # Is the noun here?
                                if noun in [item.get_name() for item in current_location.get_location_items()]:
                                    # Is noun a container?
                                    if noun in [item.get_name() for item in Container.containers]:
                                        # Get the container.
                                        for container in Container.containers:
                                            if noun == container.get_name():
                                                # If locked
                                                if container.get_locked_status():
                                                    print(f"The {container.get_name()} is locked.")
                                                # If not locked
                                                else:
                                                    container.open_container()
                                                    print(f"{container.get_name()} opened.\n"
                                                          f"{container.get_full_container_text()}")
                                    # Invalid
                                    else:
                                        print(f"{noun} cannot be opened..")
                                # Invalid.
                                else:
                                    print(f"There is no {noun} here.")
                            # Invalid.
                            else:
                                print(f"{noun} is not a valid item.")

                        # If the player wants to take something and put it in their bag.
                        elif action == "TAKE" or action == "T":
                            # Is the noun an item that can be moved?
                            if noun in [item.get_name() for item in Movable.movable_nouns]:
                                # Is the subject located in the current location?
                                if noun in [item.get_name() for item in current_location.get_location_items()]:
                                    # Find the item.
                                    for item in current_location.get_location_items():
                                        if item.get_name() == noun:
                                            # If item is visible.
                                            if item.get_visibility_status():
                                                # If getting the item has a condition to meet before being taken.
                                                if isinstance(item, Conditional):
                                                    if item.get_condition_status():
                                                        # Add it to your bag.
                                                        print(backpack.add(item))
                                                        current_location.remove_location_item(item)
                                                        # If it was revealed by another item.
                                                        if isinstance(item, RevealedMovable):
                                                            taken_from = item.get_item_revealed_by()
                                                            taken_from.item_one_taken()
                                                    else:
                                                        # New text against what happens
                                                        print(f"{item.get_name()} is out of reach.")
                                                # Trying to take water.
                                                elif item.get_name() == "WATER":
                                                    # Does the player have a water bottle?
                                                    if water_bottle in backpack.items():
                                                        # If the water bottle is already full.
                                                        if water_bottle.get_water_bottle_status():
                                                            print("The water bottle is already full.")
                                                        # If the water bottle is empty.
                                                        else:
                                                            # Fill up the water bottle.
                                                            print(water_bottle.fill_water_bottle())
                                                    # No water bottle.
                                                    else:
                                                        # Give clue.
                                                        print("I can't just put water in my bag...\n"
                                                              "If only I had a water bottle.")
                                                # Take the item.
                                                else:
                                                    # Add it to your bag.
                                                    print(backpack.add(item))
                                                    current_location.remove_location_item(item)
                                                    # If it was revealed by another item.
                                                    if isinstance(item, RevealedMovable) or \
                                                            isinstance(item, RevealedConsumable):
                                                        taken_from = item.get_item_revealed_by()
                                                        taken_from.item_one_taken()
                                                        if isinstance(item, DualRevealsMovable):
                                                            taken_from.item_two_taken()
                                                    break
                                            else:
                                                print(f"{noun} can't even be seen in this location yet.")
                                # The noun isn't located in the current location
                                else:
                                    # Invalid response.
                                    print(f"{noun} isn't located here.")
                            # The noun isn't a valid item to take.
                            else:
                                # Invalid
                                print(f"{noun} is not a valid item to {action}.")

                        # If the player wants to drop something from their bag.
                        elif action == "DROP" or action == "D":
                            # Is the noun an item?
                            if noun in [item.get_name() for item in Item.items]:
                                # Is the noun in the bag?
                                if noun in [item.get_name() for item in backpack.items()]:
                                    # Find item.
                                    for item in backpack.items():
                                        if noun == item.get_name():
                                            # Remove it and drop it in the current location.
                                            print(backpack.remove(item, current_location))
                                            print("It now lies on the ground.")
                                # Invalid
                                else:
                                    print(f"You aren't carrying a {noun} in your bag to drop.")
                            # Invalid.
                            else:
                                print(f"{noun} is not a valid item.")

                                # If the player wants to talk to a NPC.

                        # If the player wants to speak to a NPC
                        elif action == "SPEAK" or action == "S":
                            if noun == "MERMAN":
                                # Is the noun here?
                                if merman in current_location.get_location_items():
                                    # Is it visible?
                                    if merman.get_visibility_status():
                                        # Initial dialogue.
                                        print(f"{merman.get_initial_dialogue()} (Yes / No)")
                                        response = input().upper().strip()
                                        # Respond yes.
                                        if response == "YES":
                                            # Make items visible to help.
                                            if ability == "CHARISMA":
                                                jerry.make_visible()
                                                cable.make_visible()
                                                print("I can't help you escape this island, "
                                                      "you're too weak in the water.\n"
                                                      "I saw a jerry and a cable in the water to the North though.")

                                            # If items he can help get haven't been discovered.
                                            if not jerry.get_visibility_status() \
                                                    and not cable.get_visibility_status():
                                                print("I can't help you escape this island, "
                                                      "you're too weak in the water.\n"
                                                      "If there is something else, come back and see me.")
                                            # Items discovered.
                                            else:
                                                print("I could help you get the jerry or cable, "
                                                      "but it will cost you a some gold.")
                                                # Nothing in bag to trade.
                                                if coin not in backpack.items() \
                                                        and trident not in backpack.items():
                                                    if ability == "CHARISMA":
                                                        print("There is a lost Trident and Coin on The Island.\n"
                                                              "If you bring me either of them, I will help you.")
                                                    else:
                                                        print("Come back when you have something to trade.")
                                                # Item in bag to trade.
                                                else:
                                                    # Get items available to trade.
                                                    trade_items = []
                                                    trade_items_string = ""
                                                    for item in backpack.items():
                                                        if item is coin or item is trident:
                                                            trade_items.append(item)
                                                            trade_items_string += \
                                                                f"{item.get_name().capitalize()} / "

                                                    # Get items available to get from the ocean.
                                                    ocean_items = []
                                                    ocean_items_string = ""
                                                    if not buoy.item_one_taken():
                                                        ocean_items.append(buoy.get_revealed_item()[0])
                                                        ocean_items_string += \
                                                            f"{buoy.get_revealed_item()[0].get_name().capitalize()} / "
                                                    if not buoy.item_two_taken():
                                                        ocean_items.append(buoy.get_revealed_item()[1])
                                                        ocean_items_string += \
                                                            f"{buoy.get_revealed_item()[1].get_name().capitalize()} / "

                                                    # Get input.
                                                    print(f"What do you have to trade? "
                                                          f"({trade_items_string[:-3]})")
                                                    payment = input("- ").upper().strip()
                                                    payment_item = None
                                                    # Trade coin.
                                                    if payment == "COIN" and coin in trade_items:
                                                        print(backpack.remove(coin, current_location))
                                                        current_location.remove_location_item(coin)
                                                        payment_item = coin

                                                    # Trade trident.
                                                    elif payment == "TRIDENT" and trident in trade_items:
                                                        print(backpack.remove(trident, current_location))
                                                        current_location.remove_location_item(trident)
                                                        payment_item = trident
                                                    # Invalid
                                                    else:
                                                        print(f"{payment} is worthless to me.\n"
                                                              f"Return when you have something better.")

                                                    if payment_item is not None:
                                                        print(f"Want me to get the CABLE or the JERRY? "
                                                              f"({ocean_items_string[:-3]})")
                                                        response = input("- ").upper().strip()
                                                        # Want cable.
                                                        if response == "CABLE" and not buoy.item_one_taken_status():
                                                            print("I'll be back in a minute.")
                                                            time.sleep(1)
                                                            print(backpack.add(cable))
                                                            buoy.item_one_taken()
                                                            loc_six.remove_location_item(cable)
                                                            print("Pleasure doing business with you.")
                                                        # Want jerry.
                                                        elif response == "JERRY" and not buoy.item_two_taken_status():
                                                            print("I'll be back in a minute.")
                                                            time.sleep(1)
                                                            print(backpack.add(jerry))
                                                            buoy.item_two_taken()
                                                            loc_six.remove_location_item(jerry)
                                                            print("Pleasure doing business with you.")
                                                        else:
                                                            print(f"There isn't a {response} underwater.\n"
                                                                  f"Take your {payment} back.")
                                                            print(backpack.add(payment_item))
                                                        payment_item = None
                                        # Respond no.
                                        elif response == "NO":
                                            print("Be on your way then.")
                                        # Any other response.
                                        else:
                                            print(f"{response}... Don't play games. Go away then.")
                                    # Invalid.
                                    else:
                                        print(f"{noun} isn't here anymore...")
                                # Invalid.
                                else:
                                    print(f"The is no {noun} here.")

                            elif noun == "PARROT":
                                # Is the noun here?
                                if parrot in current_location.get_location_items():
                                    # If the coin is still there.
                                    if not ship.item_two_taken_status():
                                        # Do you have crackers?
                                        if crackers in backpack.items():
                                            # Get input.
                                            print(f"Give CRACKERS (Yes / No)")
                                            response = input("- ").upper().strip()
                                            # Give crackers.
                                            if response == "YES":
                                                print(backpack.remove(crackers, current_location))
                                                current_location.remove_location_item(crackers)
                                                print("Squawk. Let me give you something in return.")
                                                print("Be right back.")
                                                time.sleep(2)
                                                print("Here, have a gold coin.")
                                                print(backpack.add(coin))
                                                ship.item_two_taken()
                                                loc_nine.remove_location_item(coin)
                                            # Any other response.
                                            else:
                                                print(f"{parrot.get_initial_dialogue()}")
                                        elif ability == "CHARISMA":
                                            consumables = list()
                                            consumables_string = ""
                                            for item in backpack.items():
                                                if isinstance(item, Consumable):
                                                    consumables.append(item)
                                                    consumables_string += f"{item.get_name().capitalize()} / "
                                            if len(consumables) > 0:
                                                print(f"{parrot.get_initial_dialogue()}")
                                                print("I don't have any crackers...")
                                                print(f"But I do have ({consumables_string[:-3]})")
                                                give_parrot = input("- ").strip().upper()
                                                given = False
                                                for item in consumables:
                                                    if item.get_name() == give_parrot:
                                                        print(backpack.remove(item, current_location))
                                                        given = True
                                                        current_location.remove_location_item(item)
                                                        print("Squawk. Let me give you something in return.")
                                                        print("Be right back.")
                                                        time.sleep(2)
                                                        print("Here, have a gold coin.")
                                                        coin.make_visible()
                                                        coin.condition_met()
                                                        ship.item_two_taken()
                                                        loc_nine.remove_location_item(coin)
                                                        print(backpack.add(coin))
                                                if not given:
                                                    print(f"Squawk. You don't have a {give_parrot}")
                                            else:
                                                print("I don't have any food to give you, sorry.")

                                        # No crackers to give.
                                        else:
                                            print(f"{parrot.get_initial_dialogue()}")
                                    else:
                                        print("Squawk. Thanks for the food.")
                                # Invalid.
                                else:
                                    print(f"The is no {noun} here.")

                                given = False

                            elif noun == "KRAKEN":
                                print(f"{kraken.get_initial_dialogue()}\n"
                                      f"You have {2 - kraken_block_attempts} attempts left.")

                            else:
                                # Is the noun here?
                                if noun in [item.get_name() for item in current_location.get_location_items()]:
                                    print(f"{noun} can't talk")
                                # Invalid.
                                else:
                                    print(f"The is no {noun} here.")

                        # If the player wants to eat or drink something
                        elif action == "EAT" or action == "E":
                            # Is the noun an item.
                            if noun in [item.get_name() for item in Item.items]:
                                # Is the noun here?
                                if noun in [item.get_name() for item in current_location.get_location_items()] or \
                                        noun in [item.get_name() for item in backpack.items()]:
                                    # Is the noun consumable?
                                    if noun in [item.get_name() for item in Consumable.consumable_nouns]:
                                        # Get consumable.
                                        consumable = None
                                        for item in Consumable.consumable_nouns:
                                            if item.get_name() == noun:
                                                consumable = item
                                        # If it is visible.
                                        if consumable.get_visibility_status():
                                            if consumable is water_bottle and not water_bottle.get_water_bottle_status():
                                                print(f"The {water_bottle.get_name()} is empty.")
                                            else:
                                                if consumable is water:
                                                    pass
                                                elif consumable is water_bottle:
                                                    water_bottle.empty_water_bottle()
                                                # If it's not water.
                                                elif consumable is not water:
                                                    # Remove consumable
                                                    if consumable in current_location.get_location_items():
                                                        current_location.remove_location_item(consumable)
                                                    elif consumable in backpack.items():
                                                        backpack.remove(consumable, current_location)
                                                        current_location.remove_location_item(consumable)

                                                print(consumable.item_consumed())
                                                # Apply consumable values.
                                                energy += consumable.get_energy_value()
                                                if energy > 10:
                                                    energy = 10
                                                hydration += consumable.get_hydration_value()
                                                if hydration > 10:
                                                    hydration = 10
                                                # If the consumable had negative effects.
                                                if energy < 0 or hydration < 0:
                                                    land_death_end = True
                                                    break
                                                # New energy and hydration levels.
                                                print(f"You now have enough energy for {energy} moves.")
                                                print(f"You now have enough hydration for {hydration} moves.")
                                        else:
                                            print(f"{noun} can be seen... yet.")
                                    # Invalid.
                                    else:
                                        print(f"{noun} can not be {action}")
                                # Invalid.
                                else:
                                    print(f"There is no {noun} here.")
                            # Invalid.
                            else:
                                print(f"{noun} is not a valid item.")

                        # Invalid action.
                        else:
                            print(f"{action} is not a valid action to use with a CAPITALIZED NOUN.")

                        # Varify energy and hydration for another move.
                        if energy < 0:
                            print("Starvation takes hold as you try to get to the next location."
                                  "With no energy to continue, you close your eyes for the last time...")
                            land_death_end = True
                            print(f"\nPress [ENTER] to continue.")
                            input("- ")
                        elif hydration < 0:
                            print("Dehydration takes hold as you try to get to the next location."
                                  "The world is spinning as you close your eyes for the last time...")
                            land_death_end = True
                            print(f"\nPress [ENTER] to continue.")
                            input("- ")

    # Complete game by taking boat.
    clear_screen()
    if boat_end:
        typing(f"'Coastguard. This is {player_name}. Are you receiving. Over'")
        typing(f"'{player_name}. This is Coastguard. Receiving. Over'")
        typing(f"'{player_name}. I have found a boat and got it started. Break'")
        typing("'Making my way to your position now. Over'")
        typing("'Coastguard. Glad to hear it. We'll be waiting. Over'")
        typing(f"'{player_name}. Roger. Out'")
        print(f"\nCongratulations {player_name}. You have successfully made it off The Island.")
    # Complete game by taking kraken.
    elif kraken_end:
        typing(f"\n'Coastguard. This is {player_name}. Are you receiving. Over'")
        typing(f"'{player_name}. This is Coastguard. Receiving. Over'")
        typing(f"'{player_name}. Making my way to your position now. Break'")
        typing("'I'm coming by alternate means. Over'")
        typing("'Coastguard. Acknowledged. We'll see you soon. Over'")
        typing(f"'{player_name}. Roger. Out'")
        print(f"\nCongratulations {player_name}. You have successfully made it off The Island.")
    # Lose game by dying in the ocean.
    elif ocean_death_end:
        typing("\n'Zero Alpha. This is Coastguard. Are you receiving. Over'")
        typing("'Coastguard. This is Zero Alpha. Receiving. Over'")
        typing(f"'Coastguard. We have {player_name}. Well what's left of them. Break'")
        typing("'Their body floated past while we were waiting. Over'")
        typing("'Zero Alpha. Acknowledged. You're clear to return to base. Over'")
        typing("'Coastguard. Roger. Out'")
        print(f"\nGAME OVER {player_name}. You didn't make it off The Island alive.")
    # Lose game by dying on land.
    elif land_death_end:
        typing("\n'Zero Alpha. This is Coastguard. Are you receiving. Over'")
        typing("'Coastguard. This is Zero Alpha. Receiving. Over'")
        typing("'Coastguard. Seeking permission to return to base. Break'")
        typing("'We have been waiting here a week. Break'")
        typing(f"'{player_name} must have perished on The Island. Over'")
        typing("'Zero Alpha. Acknowledged. You're clear to return to base. Over'")
        typing("'Coastguard. Roger. Out'")
        print(f"\nGAME OVER {player_name}. You didn't make it off The Island alive.")

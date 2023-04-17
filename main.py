import time
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


def typing(string):
    for letter in string:
        print(letter, end='', flush=True)
        time.sleep(0.01)
    time.sleep(0.5)


def Introduction():
    typing("'Any callsign. This is Coastguard. Are you receiving. Over'\n")
    time.sleep(1)
    typing("'Any callsign. Any callsign'\n")
    time.sleep(0.5)
    typing("'This is. This is'\n")
    time.sleep(0.5)
    typing("'Coastguard. Coastguard'\n")
    time.sleep(0.5)
    typing("'Are you receiving. Are you receiving'\n")
    time.sleep(0.5)
    typing("'Over'\n\n")
    time.sleep(0.5)
    print("You open your eyes, the bright sun blinds you for a moment.")
    print("You grab the radio.\n")
    time.sleep(2)
    typing("'Coastguard. This is...'\n")
    time.sleep(0.5)
    print("Who am I again?")
    player_name_input = input("- ").capitalize().strip()
    typing(f"'Coastguard. This is {player_name_input}. Receiving. Over'\n")
    time.sleep(0.5)
    typing(f"'Coastguard. Glad we found you {player_name_input}. We have been looking for you for days. Break'\n")
    time.sleep(0.5)
    typing("'We can't make it to The Island, you're going to have to get to us. Break'\n")
    time.sleep(0.5)
    typing("'We're anchored twenty nautical miles to the South. Over'\n")
    time.sleep(0.5)
    typing(f"'{player_name_input}. Acknowledged. I will let you know when I'm on the way. Over'\n")
    time.sleep(0.5)
    typing("'Coastguard. Roger. If you need any help, type 'help' and press [ENTER]. Out'\n")
    time.sleep(0.5)
    return player_name_input


def load_location_items(load_location):
    # Display all static items
    for location_item in load_location.items:
        if location_item.is_visible and type(location_item) is not Movable:
            location_item.discovered = True
            print(location_item.location_text)
    # Display movable items that haven't been moved.
    for location_item in location.items:
        if location_item.is_visible and type(location_item) is Movable and not location_item.moved:
            location_item.discovered = True
            print(location_item.location_text)
    # Display dropped items
    for location_item in location.items:
        if type(location_item) is Movable and location_item.moved:
            print(f"On the ground lies the dropped {location_item.name}")
    # Options for movement.
    print(f"\nTo the North {Location.locations[location.north].cardinal_description}")
    print(f"To the East {Location.locations[location.east].cardinal_description}")
    print(f"To the South {Location.locations[location.south].cardinal_description}")
    print(f"To the West {Location.locations[location.west].cardinal_description}")


if __name__ == '__main__':
    # Keep track of objectives.
    boat_finish = False
    kraken_finish = False
    death_finish = False

    # Keep track of the current location.
    moves = 0
    current_location_index = 0
    current_location = Location.locations[current_location_index]

    # Load all the items into their respective locations.
    for location in ExplorableLocation.locations:
        for item in Base.items:
            if item.location == location.location_id:
                location.items.append(item)

    # Start
    player_name = "Bob"
    # player_name = Introduction()
    while boat_finish is False and kraken_finish is False and death_finish is False:
        # Get the current location information.
        for location in Location.locations:
            if location.location_id == current_location_index:
                move = False

                # For undiscovered locations (You arrive at...)
                if moves == 0:
                    print(f"You look around and realise you're on {location.start_text}")
                    location.discovered = True
                else:
                    if not location.discovered:
                        print(f"You arrive at {location.location_description}")
                        location.discovered = True
                    # For discovered locations (You return to...)
                    else:
                        print(f"You return to {location.location_description}")

                # Print in all the items and options for the location.
                load_location_items(current_location)

                # While the player hasn't moved.
                while not move:
                    print("\nWhat do you want to do? (Refresh / Help / Action + Subject)")
                    player_input = input("- ").strip().upper().split(" ", 1)
                    # If the player didn't enter anything.
                    if player_input[0] == "":
                        print("Did not enter anything.")
                    # If the player entered one word.
                    elif len(player_input) == 1:
                        # The player wants to the items and choices rewritten.
                        if player_input[0] == "REFRESH":
                            load_location_items(current_location)
                        # The player needs help.
                        elif player_input[0] == "HELP":
                            typing(f"'Coastguard. This is {player_name}. Are you receiving. Over'\n")
                            time.sleep(0.5)
                            typing(f"'{player_name}. This is Coastguard. Receiving. What can we help. Over'\n")
                            while True:
                                print("What would you like help with? (Basics / Goals / Actions / Nothing)")
                                response = input("- ").upper().strip()
                                typing(f"'{player_name}. {response}. Over'\n")
                                if response == "BASICS":
                                    typing("'Coastguard. You are currently on The Island. Break'\n")
                                    typing("'Anything that is of importance will be written in CAPITALS. Break'\n")
                                    typing("'Do not wander into the water, it's too dangerous. Break'\n")
                                    typing("'You need to get to us, we're 20km to the South. Break'\n")
                                    typing("'Can we help you with anything else. Over'\n")
                                elif response == "GOALS":
                                    typing("'Coastguard. You need to get to us. Break'\n")
                                    typing("'Find a boat, get it working or by any other means you can. Break'\n")
                                    typing("'Can we help you with anything else. Over'\n")
                                elif response == "ACTIONS":
                                    typing("'Coastguard. You can use the following actions on The Island. Break'\n")
                                    typing("'Refresh / Help. Break'\n")
                                    typing("'These do not require anything else. Break'\n")
                                    typing("'Inspect / Interact / Open / Close / Take / Drop / Talk / Move. Break''\n")
                                    typing("'These require a subject to work with. Break'\n")
                                    typing("'Simply type what you want to do followed by the [ENTER] key. Break'\n")
                                    typing("'Do you require more information on any of these. Over'\n")
                                    while True:
                                        print("(Refresh / Help / Inspect / Interact / Open / Take / Drop / Talk / "
                                              "Move / None)")
                                        response = input("- ").upper().strip()
                                        typing(f"'{player_name}. {response}. Over'\n")
                                        if response == "Refresh":
                                            typing("'Coastguard. Sometimes there is too much information. Break'\n")
                                            typing("'Or the screen may become crowded, making you lose track. Break'\n")
                                            typing("'This will reprint all the information for the location. Break'\n")
                                            typing("'Do you need more information on any others. Over'\n")
                                        elif response == "HELP":
                                            typing("'Coastguard. This will get you in touch with us again. Break'\n")
                                            typing("'We are here whenever you need us. Break'\n")
                                            typing("'Do you need more information on any others. Over'\n")
                                        elif response == "INSPECT":
                                            typing("'Coastguard. This gives you information about an item. Break'\n")
                                            typing("'It may reveal more items. Break'\n")
                                            typing("'It needs a subject ie. Inspect Pole. Break'\n")
                                            typing("'Do you need more information on any others. Over'\n")
                                        elif response == "INTERACT":
                                            typing("'Coastguard. If you have an item in you bag. Break'\n")
                                            typing("'And you think you can use it with another item. Break'\n")
                                            typing("'Or you need to enter a code or something. Break'\n")
                                            typing("'It needs a subject ie. Interact Ball. Break'\n")
                                            typing("'and will only work if you have the bat in your bag. Break'\n")
                                            typing("'Do you need more information on any others. Over'\n")
                                        elif response == "OPEN":
                                            typing("'Coastguard. Sometimes things will be closed. Break'\n")
                                            typing("'You can open them with this, if they aren't locked. Break'\n")
                                            typing("'You can also open you Bag and Map. Break'\n")
                                            typing("'It needs a subject ie. Open Door. Break'\n")
                                            typing("'Do you need more information on any others. Over'\n")
                                        elif response == "TAKE":
                                            typing("'Coastguard. There are many movable things on The Island. Break'\n")
                                            typing("'You can pick them up to put in your bag. Break'\n")
                                            typing("'It needs a subject ie. Take Hat. Break'\n")
                                            typing("'Do you need more information on any others. Over'\n")
                                        elif response == "DROP":
                                            typing("'Coastguard. If you need to make room in your bag. Break'\n")
                                            typing("'Drop a item. It will remain there if you want it again. Break'\n")
                                            typing("'It needs a subject ie. Drop Hat. Break'\n")
                                            typing("'Do you need more information on any others. Over'\n")
                                        elif response == "TALK":
                                            typing("'Coastguard. I hear there are other being on The Island. Break'\n")
                                            typing("'They may be able to help you, so talk to them. Break'\n")
                                            typing("'It needs a subject ie. Talk Pirate. Break'\n")
                                            typing("'Do you need more information on any others. Over'\n")
                                        elif response == "MOVE":
                                            typing("'Coastguard. Your going to have to move around. Break'\n")
                                            typing("'Use cardinal directions to go in that direction. Break'\n")
                                            typing("'It needs a subject ie. Move North. Break'\n")
                                            typing("'Do you need more information on any others. Over'\n")
                                        elif response == "NONE":
                                            typing("'Coastguard. Roger. Anything else I can help you with. Over'\n")
                                            break
                                        else:
                                            typing(f"'Coastguard. You are broken and unreadable. Say again. Over'\n")
                                elif response == "NOTHING":
                                    typing(f"'Coastguard. Roger. Out'\n")
                                    break
                                else:
                                    typing(f"'Coastguard. You are broken and unreadable. Say again. Over'\n")
                    # If the player entered move than one word.
                    elif len(player_input) >= 1:
                        # Split into the action they want to do.
                        action = player_input[0]
                        # And the item to do it upon.
                        subject = player_input[1]

                        # If the player wants to move to another location.
                        if action == "MOVE":
                            # To move to the location to the North.
                            if subject == "NORTH":
                                # If North goes into the sea.
                                move = True
                                moves += 1
                                if type(Location.locations[location.north]) is SeaLocation:
                                    print(Location.locations[location.north].location_description)
                                    death_finish = True
                                # If North goes to an explorable location.
                                else:
                                    current_location_index = location.north
                                    current_location = Location.locations[current_location_index]

                            # To move to the location to the East.
                            elif subject == "EAST":
                                move = True
                                moves += 1
                                # If East goes into the sea.
                                if type(Location.locations[location.east]) is SeaLocation:
                                    print(Location.locations[location.east].location_description)
                                    death_finish = True

                                # If East goes to an explorable location.
                                else:
                                    current_location_index = location.east
                                    current_location = Location.locations[current_location_index]

                            # To move to the location to the South.
                            elif subject == "SOUTH":
                                move = True
                                moves += 1
                                # If South goes into the sea.
                                if type(Location.locations[location.south]) is SeaLocation:
                                    print(Location.locations[location.south].location_description)
                                    death_finish = True

                                # If South goes to an explorable location.
                                else:
                                    current_location_index = location.south
                                    current_location = Location.locations[current_location_index]

                            # To move to the location to the West.
                            elif subject == "WEST":
                                move = True
                                moves += 1
                                # If West goes into the sea.
                                if type(Location.locations[location.west]) is SeaLocation:
                                    print(Location.locations[location.west].location_description)
                                    death_finish = True

                                # If West goes to an explorable location.
                                else:
                                    current_location_index = location.west
                                    current_location = Location.locations[current_location_index]

                            else:
                                print(f"The input {subject} is not a valid direction.\n"
                                      f"MOVE (North / East / South / West)")

                        # If the player wants to inspect something.
                        elif action == "INSPECT":
                            # Is the subject an item?
                            if subject in [item.name for item in Base.items]:
                                # Is the subject located in the current location?
                                if subject in [item.name for item in Location.locations[current_location_index].items]:
                                    # Find the item.
                                    for item in Location.locations[current_location_index].items:
                                        if item.name == subject:
                                            # Inspect it.
                                            print(item.inspect())
                                # Is the subject located in the players bag?
                                elif subject in [item.name for item in backpack.items()]:
                                    # Find the item.
                                    for item in backpack.items():
                                        if item.name == subject:
                                            # Inspect it.
                                            print(item.inspect())
                                else:
                                    print(f"{subject} isn't located here or in your bag.")
                            else:
                                print(f"{subject} is not a valid item to INSPECT.")

                        # If the player wants to take something and put it in their bag.
                        elif action == "TAKE":
                            # Is the subject an item that can be taken?
                            if subject in [item.name for item in Movable.movable_items] or subject == "ROCK":
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
                                                        print(backpack.add(item))
                                                        # Remove it from the location.
                                                        Location.locations[current_location_index].items.remove(item)
                                                        # If it was revealed by another item.
                                                        if isinstance(item, RevealedMovable):
                                                            taken_from = item.revealed_by
                                                            taken_from.item_one_taken = True
                                                    else:
                                                        # New text against what happens
                                                        print(f"{item.name} is out of reach.")
                                                elif item.name == "ROCK":
                                                    if backpack.rock:
                                                        print("You already have a ROCK in your bag")
                                                    else:
                                                        backpack.rock = True
                                                        print(f"ROCK added to your BAG.")

                                                elif item.name == "COCONUT":
                                                    if backpack.coconut:
                                                        print("You already have a COCONUT in your bag")
                                                    else:
                                                        backpack.coconut = True
                                                        coconut_consumable.is_visible = False
                                                        print(f"COCONUT added to your BAG.")
                                                # Take the item.
                                                else:
                                                    # Add it to your bag.
                                                    print(backpack.add(item))
                                                    # Remove it from the location.
                                                    Location.locations[current_location_index].items.remove(item)
                                                    # If it was revealed by another item.
                                                    if isinstance(item, RevealedMovable) or \
                                                            isinstance(item, RevealedConsumable):
                                                        taken_from = item.revealed_by
                                                        taken_from.item_one_taken = True
                                                        if isinstance(item, DualRevealsMovable):
                                                            taken_from.item_two_taken = True
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

                        # If the player wants to interact with something.
                        elif action == "INTERACT":
                            # Insert something to be able to turn the key chamber in the dashboard.
                            if subject == "DASHBOARD":
                                if current_location_index == 0:
                                    # Boat key in bag.
                                    if boat_key in backpack.items():
                                        print(f"{boat_key.name} inserted!\n{dashboard.key_true}")
                                        dashboard.key = True
                                        # Removes key from the game.
                                        backpack.remove(boat_key, current_location)
                                        current_location.items.remove(boat_key)
                                    # Tension rod and key rake in bag.
                                    elif tension_rod in backpack.items() and key_rake in backpack.items():
                                        print(f"{tension_rod.name} applies the force!\n"
                                              f"{key_rake.name} depresses the pins!\n"
                                              f"{dashboard.key_true}")
                                        dashboard.key = True
                                        # Removes tension rod and key rake from the game.
                                        backpack.remove(tension_rod, current_location)
                                        backpack.remove(key_rake, current_location)
                                        current_location.items.remove(tension_rod)
                                        current_location.items.remove(key_rake)
                                    # If the player doesn't have the required items.
                                    else:
                                        print("You don't have any way to turn the key in your bag...")
                                else:
                                    print(f"The is no {subject} here.")

                            elif subject == "COMPARTMENT":
                                if current_location_index == 0:
                                    if battery in backpack.items():
                                        print(f"{battery.name} inserted!\n{compartment.battery_true}")
                                        compartment.battery = True
                                        dashboard.power = True
                                        backpack.remove(battery, current_location)
                                        current_location.items.remove(battery)
                                    elif cable in backpack.items():
                                        compartment.item_two_taken = True
                                        print(f"{cable.name} plugged in!\n{compartment.power_cable_true}")
                                        if metal_box.insert:
                                            dashboard.power = True
                                            # Removes cable from the game.
                                            backpack.remove(cable, current_location)
                                            current_location.items.remove(cable)
                                        else:
                                            print(f"Now to find somewhere to plug other other end...")
                                    else:
                                        print("I need to get a form of power supply...")
                                else:
                                    print(f"The is no {subject} here.")

                            elif subject == "FUEL TANK":
                                if current_location_index == 0:
                                    if jerry in backpack.items():
                                        dashboard.fuel = True
                                        fuel_tank.insert = True
                                        print(f"{jerry.name} emptied into the fuel tank.\n{fuel_tank.full}")
                                        fuel_tank.inspect()
                                        backpack.remove(jerry, current_location)
                                        current_location.items.remove(jerry)
                                    elif alcohol in backpack.items():
                                        dashboard.fuel = True
                                        fuel_tank.insert = True
                                        print(f"{alcohol.name} emptied into the fuel tank.\n{fuel_tank.full}")
                                        fuel_tank.inspect()
                                        backpack.remove(alcohol, current_location)
                                        current_location.items.remove(alcohol)
                                    else:
                                        print(f"I need something to fill the tank with...")
                                else:
                                    print(f"The is no {subject} here.")

                            elif subject == "METAL BOX":
                                if current_location_index == 0:
                                    if cable in backpack.items():
                                        metal_box.insert = True
                                        print(f"{cable.name} plugged in.\n{metal_box.full}")
                                        if compartment.item_two_taken:
                                            dashboard.power = True
                                            # Removes cable from the game.
                                            backpack.remove(cable, current_location)
                                            current_location.items.remove(cable)
                                        else:
                                            print(f"Now to find somewhere to plug in other other end...")
                                    else:
                                        print(f"I need to find something to plug in here...")
                                else:
                                    print(f"The is no {subject} here.")

                            elif subject == "KEYPAD":
                                if current_location_index == 0:
                                    print("Please enter the 4 digit code.")
                                    input_code = input("- ")
                                    if input_code == keypad.code:
                                        print("Correct.")
                                        heavy_chest.locked = False
                                        print(f"{heavy_chest.name} unlocked.")
                                    else:
                                        print("Incorrect")
                                else:
                                    print(f"The is no {subject} here.")

                            elif subject == "HANGING COCONUT":
                                if current_location_index == 2:
                                    if coconut_item.is_visible:
                                        if rock in backpack.items():
                                            coconut_consumable.is_visible = True
                                            print(f"A perfect hit.\n{coconut_consumable.location_text}")
                                            backpack.rock = False
                                        else:
                                            print(
                                                "The COCONUT is out of reach.\nYou need something to throw at them...")
                                    else:
                                        print("Maybe I should see if there are HANGING COCONUT in the PALM first.")
                                else:
                                    print(f"The is no {subject} here.")

                            elif subject == "SAND":
                                if current_location_index == 4:
                                    if shovel in backpack.items():
                                        sand.condition_met = True
                                        print(f"What have we here.\n{sand.reveal_text}")
                                        revealed_item = sand.reveals
                                        revealed_item.is_visible = True
                                        revealed_item.discovered = True
                                        # Removes shovel from the game.
                                        backpack.remove(shovel, current_location)
                                        current_location.items.remove(shovel)
                                    else:
                                        print("The sharp shells cut your hands.\nYou need something to dig with...")
                                else:
                                    print(f"The is no {subject} here.")

                            elif subject == "WATER":
                                if current_location_index == 4:
                                    if water_bottle in backpack.items():
                                        if water_bottle.is_full:
                                            print("The water bottle is already full")
                                        else:
                                            water_bottle.is_full = True
                                            print("You fill up your water bottle.")
                                else:
                                    print(f"The is no {subject} here.")

                            elif subject == "BLOCK":
                                if current_location_index == 10:
                                    while True:
                                        slots = [block.slot_one, block.slot_two, block.slot_three]
                                        available_slots = []
                                        available_slots_string = ""
                                        occupied_slots = []
                                        occupied_slots_string = ""
                                        for i, slot in enumerate(slots):
                                            if slot is None:
                                                available_slots.append(str(i + 1))
                                                available_slots_string += f"{str(i + 1)} / "
                                            else:
                                                occupied_slots.append(str(i + 1))
                                                occupied_slots_string = f"{str(i + 1)} / "

                                        numbered_blocks = []
                                        for item in backpack.items():
                                            if item.name.startswith("BLOCK"):
                                                numbered_blocks.append(item)
                                        numbered_blocks_string = " / ".join(
                                            numbered_block.name.split()[1] for numbered_block in numbered_blocks)
                                        print(f"Would you like to insert or take a BLOCK? "
                                              f"(Insert / Take / Leave)")
                                        action_choice = input("- ").upper().strip()
                                        if action_choice == "INSERT":
                                            print(f"Into which slot would you like to insert a block? "
                                                  f"({available_slots_string}Leave)")
                                            slot_choice = input("- ").upper().strip()
                                            if slot_choice in available_slots:
                                                print(f"Which block would you like to insert? "
                                                      f"({numbered_blocks_string} / Leave)")
                                                numbered_block_choice = input("- ").upper().strip()
                                                if numbered_block_choice in [numbered_block.name.split()[1] for
                                                                             numbered_block in numbered_blocks]:
                                                    for numbered_block in numbered_blocks:
                                                        if numbered_block_choice == numbered_block.name.split()[1]:
                                                            if slot_choice == "1":
                                                                print(backpack.remove(numbered_block, current_location))
                                                                block.slot_one = numbered_block
                                                                print(f"Slot 1 now contains {numbered_block.name}")
                                                                break
                                                            elif slot_choice == "2":
                                                                print(backpack.remove(numbered_block, current_location))
                                                                block.slot_two = numbered_block
                                                                print(f"Slot 2 now contains {numbered_block.name}")
                                                                break
                                                            elif slot_choice == "3":
                                                                print(backpack.remove(numbered_block, current_location))
                                                                block.slot_three = numbered_block
                                                                print(f"Slot 3 now contains {numbered_block.name}")
                                                                break
                                                            elif slot_choice == "LEAVE":
                                                                break
                                                            else:
                                                                pass
                                                elif numbered_block_choice == "LEAVE":
                                                    break
                                                else:
                                                    print(f"Block {numbered_block_choice} is not a valid option.")
                                            elif slot_choice == "LEAVE":
                                                break
                                            else:
                                                print(f"Slot {slot_choice} is not a valid option.")

                                            if block.slot_one == block_six and \
                                                    block.slot_two == block_zero and \
                                                    block.slot_three == block_five:
                                                kraken_finish = True

                                            elif all(slot is not None for slot in
                                                     [block.slot_one, block.slot_two, block.slot_three]):
                                                print("Hmm, that can't be right. Nothing is happening...")

                                        elif action_choice == "TAKE":
                                            print(block.inspect())
                                            print(f"Which slot do you want to take a BLOCK from? "
                                                  f"({occupied_slots_string}Leave)")
                                            take_choice = input("- ").upper().strip()
                                            if take_choice == "1":
                                                print(backpack.add(block.slot_one))
                                                block.slot_one = None
                                                print(f"Slot 1 is now empty")
                                                break
                                            elif take_choice == "2":
                                                print(backpack.add(block.slot_two))
                                                block.slot_two = None
                                                print(f"Slot 2 is now empty")
                                                break
                                            elif take_choice == "3":
                                                print(backpack.add(block.slot_three))
                                                block.slot_three = None
                                                print(f"Slot 3 is now empty")
                                                break
                                            elif take_choice == "LEAVE":
                                                break
                                            else:
                                                pass

                                        elif action_choice == "LEAVE":
                                            break
                                        else:
                                            print(f"{action_choice} is not a valid input.")

                            else:
                                print(f"{subject} is not a valid item to {action} with.")

                        # To complete later
                        elif action == "OPEN":
                            if subject == "BAG":
                                print(f"Your BAG currently had {backpack.count()} items.")
                                backpack.list()
                            else:
                                for container in Container.containers:
                                    if subject == container.name:
                                        if container.locked:
                                            print(f"The {container.name} is locked.")
                                        else:
                                            container.open = True
                                            print(f"{container.name} opened.")

                                    else:
                                        print(f"{container.name} cannot be opened.")

                        # If the player wants to drop something from their bag.
                        elif action == "DROP":
                            # Is the subject an item.
                            if subject in [item.name for item in Base.items]:
                                # Find the item.
                                for item in Base.items:
                                    if subject == item.name:
                                        # Remove it and drop it in the current location.
                                        print(backpack.remove(item, Location.locations[current_location_index]))
                                        print("It now lies on the ground.")

                        elif action == "TALK":
                            if subject == "MERMAN" and current_location_index == 3:
                                print(f"{merman.initial_text} (Yes / No)")
                                response = input().upper().strip()

                                if response == "NO":
                                    print("Be on your way then.")
                                elif response == "YES":
                                    if not jerry.is_visible and not cable.is_visible:
                                        print("I can't help you escape this island, you're too weak in the water.\n"
                                              "If there is something else, come back and see me.")
                                    else:
                                        print(f"You want me to get something for you (Yes / No)")
                                        response = input().upper().strip()
                                        if response == "NO":
                                            print("Be on your way then.")
                                        elif response == "YES":
                                            print("I can do that, but it will cost you a some gold...")
                                            if backpack.in_backpack(coin) < 0 and backpack.in_backpack(trident) < 0:
                                                print("Come back when you have something to trade")

                                            else:
                                                if backpack.in_backpack(coin) >= 0 and backpack.in_backpack(
                                                        trident) >= 0:
                                                    print(f"What do you have to trade? (Coin / Trident)")
                                                    payment = input().upper().strip()

                                                    if payment == "COIN":
                                                        backpack.remove(coin, current_location)
                                                        current_location.items.remove(coin)

                                                        print(f"Want me to get the CABLE or the JERRY? (Cable / Jerry)")
                                                        response = input().upper().strip()
                                                        if response == "CABLE":
                                                            print("I'll be back in a minute.")
                                                            print(backpack.add(cable))
                                                            loc_six.items.remove(cable)
                                                            print("Pleasure doing business with you.")
                                                        elif response == "JERRY":
                                                            print("I'll be back in a minute.")
                                                            print(backpack.add(jerry))
                                                            loc_six.items.remove(jerry)
                                                            print("Pleasure doing business with you.")
                                                        else:
                                                            print(f"I don't think there is a {response} down there.")

                                                    elif payment == "TRIDENT":
                                                        backpack.remove(trident, current_location)
                                                        current_location.items.remove(trident)

                                                        print(f"Want me to get the CABLE or the JERRY? (Cable / Jerry)")
                                                        response = input().upper().strip()
                                                        if response == "CABLE":
                                                            print("I'll be back in a minute.")
                                                            print(backpack.add(cable))
                                                            loc_six.items.remove(cable)
                                                            print("Pleasure doing business with you.")
                                                        elif response == "JERRY":
                                                            print("I'll be back in a minute.")
                                                            print(backpack.add(jerry))
                                                            loc_six.items.remove(jerry)
                                                            print("Pleasure doing business with you.")
                                                        else:
                                                            print(f"I don't think there is a {response} down there.")

                                                elif backpack.in_backpack(coin) >= 0:
                                                    print(f"What do you have to trade? (Coin)")
                                                    payment = input().upper().strip()
                                                    if payment == "COIN":
                                                        backpack.remove(coin, current_location)
                                                        current_location.items.remove(coin)

                                                        print(f"Want me to get the CABLE or the JERRY? (Cable / Jerry)")
                                                        response = input().upper().strip()
                                                        if response == "CABLE":
                                                            print("I'll be back in a minute.")
                                                            print(backpack.add(cable))
                                                            loc_six.items.remove(cable)
                                                            print("Pleasure doing business with you.")
                                                        elif response == "JERRY":
                                                            print("I'll be back in a minute.")
                                                            print(backpack.add(jerry))
                                                            loc_six.items.remove(jerry)
                                                            print("Pleasure doing business with you.")
                                                        else:
                                                            print(f"I don't think there is a {response} down there.")

                                                elif backpack.in_backpack(trident) >= 0:
                                                    print(f"What do you have to trade? (Trident)")
                                                    payment = input().upper().strip()
                                                    if payment == "TRIDENT":
                                                        backpack.remove(trident, current_location)
                                                        current_location.items.remove(trident)

                                                        print(f"Want me to get the CABLE or the JERRY? (Cable / Jerry)")
                                                        response = input().upper().strip()
                                                        if response == "CABLE":
                                                            print("I'll be back in a minute.")
                                                            backpack.add(cable)
                                                            loc_six.items.remove(cable)
                                                            print("Pleasure doing business with you.")
                                                        elif response == "JERRY":
                                                            print("I'll be back in a minute.")
                                                            backpack.add(jerry)
                                                            loc_six.items.remove(jerry)
                                                            print("Pleasure doing business with you.")
                                                        else:
                                                            print(f"I don't think there is a {response} down there.")

                                else:
                                    print("Don't play games, leave me in peace then.")

                            elif subject == "PARROT":
                                if backpack.in_backpack(crackers) >= 0:
                                    print(f"Give CRACKERS (Yes / No)")
                                    response = input().upper().strip()
                                    if response == "YES":
                                        backpack.remove(crackers, current_location)
                                        current_location.items.remove(crackers)
                                        print("Thanks, how can I help? (Coin)")
                                        response = input().upper().strip()
                                        if response == "COIN":
                                            print("Be right back.")
                                            print(backpack.add(coin))
                                            ship.item_two_taken = True
                                            loc_nine.items.remove(coin)
                                            print("There you go.")
                                    else:
                                        print(f"{parrot.initial_text}")
                                else:
                                    print(f"{parrot.initial_text}")

                            elif subject == "KRAKEN":
                                print(f"{kraken.initial_text}")

                            else:
                                print(f"{subject} can't talk")

                        elif action == "PRESS":
                            if subject == "BUTTON":
                                if current_location_index == 0:
                                    if dashboard.key is True and dashboard.power is True and dashboard.fuel is True:
                                        boat_finish = True
                                    else:
                                        print("Nothing happens...")
                                else:
                                    print(f"The is no {subject} here.")
                            else:
                                print(f"{subject} is not a valid item to {action}.")

                        else:
                            print(f"{action} is not a valid ACTION.")

    if boat_finish is True:
        print("The boat engine roars to life as you cast of the rope.")
        typing(f"'Coastguard. This is {player_name}. Are you receiving. Over'\n")
        typing(f"'{player_name}. This is Coastguard. Receiving. Over'\n")
        typing(f"'{player_name}. I have found a boat and got it started. Break'\n")
        typing("'Making my way to your position now. Over'\n")
        typing("'Coastguard. Glad to hear it. We'll be waiting. Over'\n")
        typing(f"'{player_name}. Roger. Out'\n")
        typing(f"Congratulations {player_name}. You have successfully made it off The Island.")

    elif kraken_finish is True:
        print("The water in front of you explodes\n"
              "A tentacle wraps around your body as its owner appears from the depths.\n"
              "")

    elif death_finish is True:
        typing("'Zero Alpha. This is Coastguard. Are you receiving. Over'\n")
        typing("'Coastguard. This is Zero Alpha. Receiving. Over'\n")
        typing(f"'Coastguard. We have {player_name}. Well what's left of them. Break'\n")
        typing("'Their body floated past while we were waiting. Over'\n")
        typing("'Zero Alpha. Acknowledged. You're clear to return to base. Over'\n")
        typing("'Coastguard. Roger. Out'\n")
        typing("GAME OVER. You didn't make it off The Island alive.")

    else:
        "I don't know how you got here..."

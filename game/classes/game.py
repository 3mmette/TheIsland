import time
import copy
import shutil
from os import system, name
from game.classes.backpack import BackPack
from game.classes.chart import Chart
from game.game_files.location_zero import *
from game.game_files.location_one import *
from game.game_files.location_two import *
from game.game_files.location_three import *
from game.game_files.location_four import *
from game.game_files.location_five import *
from game.game_files.location_six import *
from game.game_files.location_seven import *
from game.game_files.location_eight import *
from game.game_files.location_nine import *
from game.game_files.location_ten import *
from game.game_files.locations_surrounding import *


class Game:
    """
    This class represents the game itself. All parts of the game are run by this class.
    It creates a copy of all items to use within the game, so original files and items are not changed.
    """
    game_locations = list()
    game_items = list()

    def __init__(self):
        """
        Initialize all variables and items for the game.
        """
        self.player_name = ""
        self.ability = None
        self.energy = 10
        self.hydration = 10
        self.current_player_input = list()
        self.current_input_action = ""
        self.current_input_noun = ""

        self.boat_end = False
        self.kraken_end = False
        self.ocean_death_end = False
        self.land_death_end = False
        self.quit_end = False

        self.moved = False
        self.moves = 0
        self.kraken_block_attempts = 0

        # Game Locations.
        self.location_zero = None
        self.location_one = None
        self.location_two = None
        self.location_three = None
        self.location_four = None
        self.location_five = None
        self.location_six = None
        self.location_seven = None
        self.location_eight = None
        self.location_nine = None
        self.location_ten = None
        self.location_eleven = None
        self.location_twelve = None
        self.location_thirteen = None

        self.current_location_index = None
        self.current_location = None

        self.current_location_index = None
        self.current_location = None

        # Players Items.
        self.backpack = None
        self.chart = None

        # Location Zero Items.
        self.dashboard = None
        self.compartment = None
        self.heavy_chest = None
        self.fuel_tank = None
        self.battery = None
        self.button = None
        self.keypad = None
        self.block_zero = None

        # Location One Items
        self.sign = None
        self.paper = None
        self.metal_box = None
        self.block_one = None

        # Location Two Items
        self.palm = None
        self.coconut = None
        self.sand = None
        self.wooden_chest = None
        self.alcohol = None
        self.block_two = None

        # Location Three Items
        self.driftwood = None
        self.tension_rod = None
        self.merman = None
        self.block_three = None

        # Location Four Items
        self.spring = None
        self.water = None
        self.rock = None
        self.boat_key = None
        self.block_four = None

        # Location Five Items
        self.tree = None
        self.key_rake = None
        self.parrot = None
        self.block_five = None

        # Location Six Items
        self.water_bottle = None
        self.beans = None
        self.soup = None
        self.buoy = None
        self.cable = None
        self.jerry = None
        self.block_six = None

        # Location Seven Items
        self.fruit_tree = None
        self.body = None
        self.note = None
        self.red_fruit = None
        self.orange_fruit = None
        self.yellow_fruit = None
        self.green_fruit = None
        self.blue_fruit = None
        self.purple_fruit = None
        self.block_seven = None

        # Location Eight Items
        self.trident = None
        self.sword = None
        self.shovel = None
        self.block_eight = None

        # Location Nine Items
        self.ship = None
        self.coin = None
        self.crackers = None
        self.block_nine = None

        # Location Ten Items
        self.block = None
        self.shadow = None
        self.kraken = None

    @staticmethod
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

    @staticmethod
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

    def reset_game(self):
        """
        Resets all variables and creates a new copy of all items to use in the current game.
        """
        self.game_items = list()
        self.game_locations = list()

        self.ability = None
        self.energy = 10
        self.hydration = 10
        self.current_player_input = list()
        self.current_input_action = ""
        self.current_input_noun = ""

        self.boat_end = False
        self.kraken_end = False
        self.ocean_death_end = False
        self.land_death_end = False
        self.quit_end = False

        self.moved = False
        self.moves = 0
        self.kraken_block_attempts = 0

        # Game Locations.
        self.location_zero = copy.copy(original_location_zero)
        self.location_one = copy.copy(original_location_one)
        self.location_two = copy.copy(original_location_two)
        self.location_three = copy.copy(original_location_three)
        self.location_four = copy.copy(original_location_four)
        self.location_five = copy.copy(original_location_five)
        self.location_six = copy.copy(original_location_six)
        self.location_seven = copy.copy(original_location_seven)
        self.location_eight = copy.copy(original_location_eight)
        self.location_nine = copy.copy(original_location_nine)
        self.location_ten = copy.copy(original_location_ten)
        self.location_eleven = copy.copy(original_location_eleven)
        self.location_twelve = copy.copy(original_location_twelve)
        self.location_thirteen = copy.copy(original_location_thirteen)

        self.game_locations.append(self.location_zero)
        self.game_locations.append(self.location_one)
        self.game_locations.append(self.location_two)
        self.game_locations.append(self.location_three)
        self.game_locations.append(self.location_four)
        self.game_locations.append(self.location_five)
        self.game_locations.append(self.location_six)
        self.game_locations.append(self.location_seven)
        self.game_locations.append(self.location_eight)
        self.game_locations.append(self.location_nine)
        self.game_locations.append(self.location_ten)
        self.game_locations.append(self.location_eleven)
        self.game_locations.append(self.location_twelve)
        self.game_locations.append(self.location_thirteen)
        self.game_locations.sort(key=lambda x: x.get_location_id())

        self.current_location_index = 0
        self.current_location = self.game_locations[self.current_location_index]

        # Players Items.
        self.backpack = copy.copy(BackPack())
        self.chart = copy.copy(Chart())

        # Reset chart.
        shutil.copyfile("game/game_files/original_chart.txt", "game/game_files/chart.txt")
        self.chart.reset_chart(self.game_locations)

        # Location Zero Items.
        self.dashboard = copy.copy(original_dashboard)
        self.compartment = copy.copy(original_compartment)
        self.heavy_chest = copy.copy(original_heavy_chest)
        self.fuel_tank = copy.copy(original_fuel_tank)
        self.battery = copy.copy(original_battery)
        self.button = copy.copy(original_button)
        self.keypad = copy.copy(original_keypad)
        self.block_zero = copy.copy(original_block_zero)

        # Link any items.
        self.dashboard.set_revealed_item(self.button)
        self.heavy_chest.set_revealed_item(self.keypad)
        self.heavy_chest.set_holds_item(self.battery)
        self.battery.set_item_revealed_by(self.heavy_chest)

        # Add to game items list.
        self.game_items.append(self.dashboard)
        self.game_items.append(self.compartment)
        self.game_items.append(self.heavy_chest)
        self.game_items.append(self.fuel_tank)
        self.game_items.append(self.battery)
        self.game_items.append(self.button)
        self.game_items.append(self.keypad)
        self.game_items.append(self.block_zero)

        # Location One Items
        self.sign = copy.copy(original_sign)
        self.paper = copy.copy(original_paper)
        self.metal_box = copy.copy(original_metal_box)
        self.block_one = copy.copy(original_block_one)

        # Link any items.
        self.select_and_set_cryptic_keypad_puzzle()

        # Add to game items list.
        self.game_items.append(self.sign)
        self.game_items.append(self.paper)
        self.game_items.append(self.metal_box)
        self.game_items.append(self.block_one)

        # Location Two Items
        self.palm = copy.copy(original_palm)
        self.coconut = copy.copy(original_coconut)
        self.sand = copy.copy(original_sand)
        self.wooden_chest = copy.copy(original_wooden_chest)
        self.alcohol = copy.copy(original_alcohol)
        self.block_two = copy.copy(original_block_two)

        # Link any items.
        self.palm.set_revealed_item(self.coconut)
        self.sand.set_revealed_item(self.wooden_chest)
        self.wooden_chest.set_holds_item(self.alcohol)
        self.coconut.set_item_revealed_by(self.palm)
        self.alcohol.set_item_revealed_by(self.wooden_chest)

        # Add to game items list.
        self.game_items.append(self.palm)
        self.game_items.append(self.coconut)
        self.game_items.append(self.sand)
        self.game_items.append(self.wooden_chest)
        self.game_items.append(self.alcohol)
        self.game_items.append(self.block_two)

        # Location Three Items
        self.driftwood = copy.copy(original_driftwood)
        self.tension_rod = copy.copy(original_tension_rod)
        self.merman = copy.copy(original_merman)
        self.block_three = copy.copy(original_block_three)

        # Link any items.
        self.driftwood.set_revealed_item(self.tension_rod)
        self.tension_rod.set_item_revealed_by(self.driftwood)

        # Add to game items list.
        self.game_items.append(self.driftwood)
        self.game_items.append(self.tension_rod)
        self.game_items.append(self.merman)
        self.game_items.append(self.block_three)

        # Location Four Items
        self.spring = copy.copy(original_spring)
        self.water = copy.copy(original_water)
        self.rock = copy.copy(original_rock)
        self.boat_key = copy.copy(original_boat_key)
        self.block_four = copy.copy(original_block_four)

        # Link any items.
        self.spring.set_revealed_item(self.boat_key)
        self.boat_key.set_item_revealed_by(self.spring)

        # Add to game items list.
        self.game_items.append(self.spring)
        self.game_items.append(self.water)
        self.game_items.append(self.rock)
        self.game_items.append(self.boat_key)
        self.game_items.append(self.block_four)

        # Location Five Items
        self.tree = copy.copy(original_tree)
        self.key_rake = copy.copy(original_key_rake)
        self.parrot = copy.copy(original_parrot)
        self.block_five = copy.copy(original_block_five)

        # Link any items.
        self.tree.set_revealed_item(self.key_rake)
        self.key_rake.set_item_revealed_by(self.tree)

        # Add to game items list.
        self.game_items.append(self.tree)
        self.game_items.append(self.key_rake)
        self.game_items.append(self.parrot)
        self.game_items.append(self.block_five)

        # Location Six Items
        self.water_bottle = copy.copy(original_water_bottle)
        self.beans = copy.copy(original_beans)
        self.soup = copy.copy(original_soup)
        self.buoy = copy.copy(original_buoy)
        self.cable = copy.copy(original_cable)
        self.jerry = copy.copy(original_jerry)
        self.block_six = copy.copy(original_block_six)

        # Link any items.
        self.buoy.set_revealed_item(self.cable)
        self.buoy.set_revealed_item(self.jerry)
        self.cable.set_item_revealed_by(self.buoy)
        self.jerry.set_item_revealed_by(self.buoy)

        # Add to game items list.
        self.game_items.append(self.water_bottle)
        self.game_items.append(self.beans)
        self.game_items.append(self.soup)
        self.game_items.append(self.buoy)
        self.game_items.append(self.cable)
        self.game_items.append(self.jerry)
        self.game_items.append(self.block_six)

        # Location Seven Items
        self.fruit_tree = copy.copy(original_fruit_tree)
        self.body = copy.copy(original_body)
        self.note = copy.copy(original_note)
        self.red_fruit = copy.copy(original_red_fruit)
        self.orange_fruit = copy.copy(original_orange_fruit)
        self.yellow_fruit = copy.copy(original_yellow_fruit)
        self.green_fruit = copy.copy(original_green_fruit)
        self.blue_fruit = copy.copy(original_blue_fruit)
        self.purple_fruit = copy.copy(original_purple_fruit)
        self.block_seven = copy.copy(original_block_seven)

        # Link any items.
        self.fruit_tree.set_reveals_items_list(list())
        self.body.set_revealed_item(self.note)
        self.note.set_linked_item(self.spring)
        self.fruit_tree.set_revealed_item(self.red_fruit)
        self.red_fruit.set_item_revealed_by(self.fruit_tree)
        self.fruit_tree.set_revealed_item(self.orange_fruit)
        self.orange_fruit.set_item_revealed_by(self.fruit_tree)
        self.fruit_tree.set_revealed_item(self.yellow_fruit)
        self.yellow_fruit.set_item_revealed_by(self.fruit_tree)
        self.fruit_tree.set_revealed_item(self.green_fruit)
        self.green_fruit.set_item_revealed_by(self.fruit_tree)
        self.fruit_tree.set_revealed_item(self.blue_fruit)
        self.blue_fruit.set_item_revealed_by(self.fruit_tree)
        self.fruit_tree.set_revealed_item(self.purple_fruit)
        self.purple_fruit.set_item_revealed_by(self.fruit_tree)
        self.randomize_and_set_fruit_puzzle()

        # Add to game items list.
        self.game_items.append(self.fruit_tree)
        self.game_items.append(self.body)
        self.game_items.append(self.note)
        self.game_items.append(self.red_fruit)
        self.game_items.append(self.orange_fruit)
        self.game_items.append(self.yellow_fruit)
        self.game_items.append(self.green_fruit)
        self.game_items.append(self.blue_fruit)
        self.game_items.append(self.purple_fruit)
        self.game_items.append(self.block_seven)

        # Location Eight Items
        self.trident = copy.copy(original_trident)
        self.sword = copy.copy(original_sword)
        self.shovel = copy.copy(original_shovel)
        self.block_eight = copy.copy(original_block_eight)

        # Link any items.

        # Add to game items list.
        self.game_items.append(self.trident)
        self.game_items.append(self.sword)
        self.game_items.append(self.shovel)
        self.game_items.append(self.block_eight)

        # Location Nine Items
        self.ship = copy.copy(original_ship)
        self.coin = copy.copy(original_coin)
        self.crackers = copy.copy(original_crackers)
        self.block_nine = copy.copy(original_block_nine)

        # Link any items.
        self.ship.set_revealed_item(self.coin)
        self.coin.set_item_revealed_by(self.ship)
        self.ship.set_revealed_item(self.crackers)
        self.crackers.set_item_revealed_by(self.ship)

        # Add to game items list.
        self.game_items.append(self.ship)
        self.game_items.append(self.coin)
        self.game_items.append(self.crackers)
        self.game_items.append(self.block_nine)

        # Location Ten Items
        self.block = copy.copy(original_block)
        self.shadow = copy.copy(original_shadow)
        self.kraken = copy.copy(original_kraken)

        # Link any items.
        self.shadow.set_revealed_item(self.kraken)

        # Add to game items list.
        self.game_items.append(self.block)
        self.game_items.append(self.shadow)
        self.game_items.append(self.kraken)

    def select_and_set_cryptic_keypad_puzzle(self):
        """
        Selects and sets one of ten cryptic answers and clues within the game.
        """
        cryptic_answer_and_clue = {"ISLE": "Part of Chislehurst you can't walk away from. (4)",
                                   "SAND": "Hazard constructed in bricks and mortar. (4)",
                                   "PALM": "Handy source of coconuts. (4)",
                                   "SHIP": "Drink slowly, about an hour per schooner, say. (4)",
                                   "BOAT": "Snake on top of tea packet? (4)",
                                   "WAVE": "Greeting seen by the coast. (4)",
                                   "FISH": "Ray, for instance, is a well-known swimmer. (4)",
                                   "SALT": "Add some seasoning to the marsh. (4)",
                                   "CRAB": "Small wild apple you might find in the sea? (4)",
                                   "ROCK": "Music set in stone. (4)"}

        selected_cryptic = randint(0, 9)
        count_track = 0
        for answer, clue in cryptic_answer_and_clue.items():
            if count_track == selected_cryptic:
                self.keypad.set_access_code(answer)
                self.paper.set_description_text(f"On the paper is a cryptic clue.\n'{clue}'")
            count_track += 1

    def randomize_and_set_fruit_puzzle(self):
        """
        Randomly selects and sets the deadly fruit, and sets the other fruit accordingly.
        """
        all_fruit_colours = ["RED FRUIT", "ORANGE FRUIT", "YELLOW FRUIT", "GREEN FRUIT", "BLUE FRUIT", "PURPLE FRUIT"]
        random_death_index = randint(0, 5)
        death_fruit = [None, -100, -100, "Poisonous from the first bite, death comes swiftly."]
        bad_fruit_one = [None, -5, -5, "It makes you sick."]
        bad_fruit_two = [None, -5, -5, "It makes you sick."]
        good_fruit_one = [None, 6, 3, "Sweet and delicious."]
        good_fruit_two = [None, 6, 3, "Sweet and delicious."]
        best_fruit = [None, 10, 6, "The best piece of fruit you have ever eaten."]
        if random_death_index == 0:
            death_fruit[0] = all_fruit_colours[0]
            bad_fruit_one[0] = all_fruit_colours[1]
            bad_fruit_two[0] = all_fruit_colours[5]
            good_fruit_one[0] = all_fruit_colours[2]
            good_fruit_two[0] = all_fruit_colours[4]
            best_fruit[0] = all_fruit_colours[3]
        elif random_death_index == 1:
            death_fruit[0] = all_fruit_colours[1]
            bad_fruit_one[0] = all_fruit_colours[0]
            bad_fruit_two[0] = all_fruit_colours[2]
            good_fruit_one[0] = all_fruit_colours[5]
            good_fruit_two[0] = all_fruit_colours[3]
            best_fruit[0] = all_fruit_colours[4]
        elif random_death_index == 2:
            death_fruit[0] = all_fruit_colours[2]
            bad_fruit_one[0] = all_fruit_colours[1]
            bad_fruit_two[0] = all_fruit_colours[3]
            good_fruit_one[0] = all_fruit_colours[0]
            good_fruit_two[0] = all_fruit_colours[4]
            best_fruit[0] = all_fruit_colours[5]
        elif random_death_index == 3:
            death_fruit[0] = all_fruit_colours[3]
            bad_fruit_one[0] = all_fruit_colours[2]
            bad_fruit_two[0] = all_fruit_colours[4]
            good_fruit_one[0] = all_fruit_colours[1]
            good_fruit_two[0] = all_fruit_colours[5]
            best_fruit[0] = all_fruit_colours[0]
        elif random_death_index == 4:
            death_fruit[0] = all_fruit_colours[4]
            bad_fruit_one[0] = all_fruit_colours[3]
            bad_fruit_two[0] = all_fruit_colours[5]
            good_fruit_one[0] = all_fruit_colours[2]
            good_fruit_two[0] = all_fruit_colours[0]
            best_fruit[0] = all_fruit_colours[1]
        elif random_death_index == 5:
            death_fruit[0] = all_fruit_colours[5]
            bad_fruit_one[0] = all_fruit_colours[4]
            bad_fruit_two[0] = all_fruit_colours[0]
            good_fruit_one[0] = all_fruit_colours[3]
            good_fruit_two[0] = all_fruit_colours[1]
            best_fruit[0] = all_fruit_colours[2]

        assigned_fruits = [death_fruit, bad_fruit_one, bad_fruit_two, good_fruit_one, good_fruit_two, best_fruit]

        for item in self.fruit_tree.get_revealed_item():
            for values in assigned_fruits:
                if item.get_name() == values[0]:
                    item.set_energy_value(values[1])
                    item.set_hydration_value(values[2])
                    item.set_consumed_text(values[3])

        self.fruit_tree.set_reveals_items_list(sample(self.fruit_tree.get_revealed_item(), len(self.fruit_tree.get_revealed_item())))
        self.body.set_description_text(f"In one hand is a piece of {death_fruit[0].lower()}.\nIn the other is a NOTE.")

    def introduction_to_set_players_name(self):
        """
        Story to set the players name.
        """
        self.clear_screen()
        self.typing("'Any callsign. This is Coastguard. Are you receiving. Over'")
        time.sleep(1)
        self.typing("'Any callsign. Any callsign'")
        self.typing("'This is. This is'")
        self.typing("'Coastguard. Coastguard'")
        self.typing("'Are you receiving. Are you receiving'")
        self.typing("'Over'\n")
        time.sleep(1)
        print("You open your eyes, the bright sun blinds you for a moment.")
        print("You grab the radio.\n")
        time.sleep(1)
        self.typing("'Coastguard. This is...'")
        time.sleep(1)
        # Get players name.
        while self.player_name == "":
            print("\nWho am I again?")
            self.player_name = input("- ").capitalize().strip()

    def introduction_and_goals(self):
        """
        Give the player a goal.
        """
        self.clear_screen()
        self.typing(f"'Coastguard. This is {self.player_name}. Receiving. Over'")
        self.typing(f"'Coastguard. Glad we found you {self.player_name}. We have been looking for you for days. Break'")
        self.typing("'We can't make it to The Island, you're going to have to get to us. Break'")
        self.typing("'We're anchored twenty nautical miles to the South. Over'")
        self.typing(f"'{self.player_name}. Acknowledged. I will let you know when I'm on the way. Over'")
        self.typing("'Coastguard. Roger. If you need any further instructions on what to do. Break'")
        self.typing("'Simply type 'HELP' and press [ENTER] to call us. Out'")
        print("\nPress [ENTER] to continue.")
        input("- ")

    def get_and_set_players_special_ability(self):
        """
        Allows the player to select a special ability of their choosing.
        """
        self.clear_screen()
        print("More memories coming flooding back. I remember I was good at something...")
        time.sleep(1)
        print("\nStrength: You have the strength of an Ox, you can carry 10 items in your backpack instead of 5.")
        print("Dexterity: You are light on your feet, moving only takes energy and hydration every second turn.")
        print("Charisma: You speak well and seem to be liked naturally, others want to help you more.")
        print("Intelligence: You just seem to know more, food and drink items now have statistics.")

        while True:
            print("\nWhat was it again? (Strength / Dexterity / Charisma / Intelligence)")
            self.ability = input("- ").strip().upper()
            if self.ability == "STRENGTH":
                self.backpack.set_capacity(10)
                break
            elif self.ability == "DEXTERITY":
                break
            elif self.ability == "CHARISMA":
                self.kraken_block_attempts = -2
                break
            elif self.ability == "INTELLIGENCE":
                break
            else:
                print(f"\n{self.ability.capitalize()}... I don't think I was good at that.")

        print(f"\nAh yes, I have elite levels of {self.ability.lower()}.")

        print("\nPress [ENTER] to begin your adventure on The Island.")
        input("- ")

    def set_all_items_in_game(self):
        """
        Places all items in their respective locations by matching ID's.
        """
        for location in self.game_locations:
            if isinstance(location, ExplorableLocation):
                location.clear_location_items()
                for item in self.game_items:
                    if item.get_initial_location_id() == location.get_location_id():
                        location.add_item_to_location(item)

    def show_location_introduction_on_move(self):
        """
        When a player moves to a new location, shows the generic location information depending on its discovery status.
        """
        for location in self.game_locations:
            if location.get_location_id() == self.current_location_index:
                # Set or reset move to false.
                self.moved = False
                self.clear_screen()
                # Mark location as discovered on chart.
                if not self.current_location.get_discovery_status():
                    self.chart.location_discovered(self.current_location)
                else:
                    self.chart.add_player_location(self.current_location)

                # Starting text for first location the first time.
                if self.moves == 0:
                    print(f"You look around and realise you're on {location.get_start_text()}")
                    print(f"You have a Bag (B), which can hold {self.backpack.get_capacity()} items.")
                    print(f"You also have a Chart (C) of The Island.")
                    location.location_discovered()
                # Once the player starts moving.
                else:
                    # For undiscovered game_files (You arrive at...).
                    if not location.get_discovery_status():
                        print(f"You arrive at {location.get_location_description_text()}")
                        location.location_discovered()
                    # For discovered game_files (You return to...).
                    else:
                        print(f"You return to {location.get_location_description_text()}")

    def show_location_items_information(self):
        """
        Shows all the items located in a location.
        """
        # Display all static items
        for item in self.current_location.get_location_items():
            if item.get_visibility_status() and not isinstance(item, Movable):
                item.item_discovered()
                print(item.get_location_description_text())
            # Display movable items that haven't been moved.
            elif item.get_visibility_status() and isinstance(item, Movable) and not item.get_moved_status():
                item.item_discovered()
                print(item.get_location_description_text())
            # Display movable items that have been moved and dropped in a location.
            elif item.get_visibility_status() and isinstance(item, Movable) and item.get_moved_status():
                print(f"On the ground lies the dropped {item.get_name()}")

    def show_energy_and_hydration_information(self):
        """
        Shows how much energy and hydration the player has remaining.
        """
        print(f"\nYou currently have enough energy for {self.energy} moves.")
        print(f"You currently have enough hydration for {self.hydration} moves")

    def show_options_for_movement(self):
        """
        Shows what is located in the surrounding locations the player can move to.
        """
        print(f"\nTo the NORTH (N) {self.game_locations[self.current_location.get_north_id()].get_cardinal_description_text()}")
        print(f"To the EAST (E) {self.game_locations[self.current_location.get_east_id()].get_cardinal_description_text()}")
        print(f"To the SOUTH (S) {self.game_locations[self.current_location.get_south_id()].get_cardinal_description_text()}")
        print(f"To the WEST (W) {self.game_locations[self.current_location.get_west_id()].get_cardinal_description_text()}")

    def get_players_input_on_what_they_want_to_do(self):
        """
        Get what the player wants to do.
        """
        # Ask the player what they want to do.
        print("\nWhat do you want to do now?")
        print("Help (H) / Refresh (R) / Bag (B) / Chart (C) / Quit (Q)")
        print("Look (L) / Move (M) / Interact (I) / Open (O) / Take (T) / Drop (D) / Speak (S) / "
              "Eat (E) + CAPITALIZED NOUN")
        self.current_player_input = input("- ").strip().upper().split(" ", 1)
        print("")

    def player_needs_help(self):
        """
        If they require assistance on what to do or how to do things.
        """
        # Contact helper.
        self.typing(f"'Coastguard. This is {self.player_name}. Are you receiving. Over'")
        self.typing(f"'{self.player_name}. This is Coastguard. Receiving. How can we help. Over'")
        # Create a loop while the player still needs help.
        while True:
            # Input what they need help with.
            print("What would you like help with? (Basics / Goals / Actions / Nothing)")
            response = input("- ").upper().strip()
            self.typing(f"'{self.player_name}. {response}. Over'")
            # Need help with the basics of the game.
            if response == "BASICS":
                # Basics of the game.
                self.typing("'Coastguard. You are currently on The Island. Break'")
                self.typing("'Anything that is of importance will be written in 'CAPITALS'. Break'")
                self.typing("'Do not wander into the water, it's too dangerous. Break'")
                self.typing("'You can move around The Island to explore different areas. Break'")
                self.typing("'Remember to eat and drink. Don't want you dying on us. Break'")
                self.typing("'You need to get to us, we're 20 nautical miles to the South. Break'")
                self.typing("'Can we help you with anything else. Over'")
            # Need help with the goals of the game.
            elif response == "GOALS":
                # Goal
                self.typing("'Coastguard. You need to get to us. Break'")
                self.typing("'Find a boat, get it working or by any other means you can. Break'")
                self.typing("'Can we help you with anything else. Over'")
            # Need help with action within the game.
            elif response == "ACTIONS":
                # Basic actions.
                self.typing("'Coastguard. You can use the following actions on The Island. Break'")
                self.typing("'Help (H) / Refresh (R) / Bag (B) / Chart (C) / Quit (Q). Break'")
                self.typing("'These do not require any noun to work with. Break'")
                self.typing("'Look (L) / Move (M) / Interact (I) / Open (O) / Take (T) / Drop (D) / "
                            "Speak (S) / Eat (E). Break''")
                self.typing("'These require a CAPITALIZED NOUN to work with. Break'")
                self.typing("'Shorthand also works, with just the first letter of the action. Break'")
                self.typing("'So instead of 'Look' + Noun, use 'L' + Noun. Break'")
                self.typing("'Simply type what you want to do followed by the [ENTER] key. Break'")
                self.typing("'Do you require more information on any of these. Over'")
                # Create a loop while the player still needs help with actions.
                while True:
                    # Input what action they need help with.
                    print("(Refresh / Help / Bag / Chart / Quit / Look / Move / Interact / Open / "
                          "Take / Drop / Speak / Eat / No)")
                    response = input("- ").upper().strip()
                    self.typing(f"'{self.player_name}. {response}. Over'")
                    # Help action.
                    if response == "HELP":
                        self.typing("'Coastguard. This will get you in touch with us again. Break")
                        self.typing("'We are here whenever you need us. Break")
                        self.typing("'Do you need more information on any others. Over")
                    # Refresh action.
                    elif response == "REFRESH":
                        self.typing("'Coastguard. Sometimes there is too much information. Break'")
                        self.typing("'Or the screen may become crowded, making you lose track. Break'")
                        self.typing("'This will reprint all the information for the location. Break'")
                        self.typing("'Do you need more information on any others. Over'")
                    # Bag action.
                    elif response == "BAG":
                        self.typing("'Coastguard. You should have a bag with you. Break'")
                        self.typing("'When you take an item, it will be placed in your bag. Break'")
                        self.typing("'You can use this command to see what's in your bag. Break'")
                        self.typing("'Do you need more information on any others. Over'")
                    # Chart action.
                    elif response == "CHART":
                        self.typing("'Coastguard. You should have a chart with you. Break'")
                        self.typing("'It will give you an overview of The Island. Break'")
                        self.typing("'It will keep track of places you've been. Break'")
                        self.typing("'You can use this command to see the chart. Break'")
                        self.typing("'Do you need more information on any others. Over'")
                    # Quit action.
                    elif response == "QUIT":
                        self.typing("'Coastguard. If you don't want to adventure anymore. Break'")
                        self.typing("'This will just end the game, nothing more to it. Break'")
                        self.typing("'Do you need more information on any others. Over'")
                    # Look action.
                    elif response == "LOOK":
                        self.typing("'Coastguard. This gives you information about an item. Break")
                        self.typing("'It may reveal more items. Break")
                        self.typing("'It needs a subject ie. Look Pole / L Pole. Break")
                        self.typing("'Do you need more information on any others. Over")
                    # Move action
                    elif response == "MOVE":
                        self.typing("'Coastguard. Your going to have to move around. Break'")
                        self.typing("'Use cardinal directions to go in that direction. Break'")
                        self.typing("'It needs a subject ie. Move North / M North. Break'")
                        self.typing("'You can shorthand the direction too ie. M N. Break'")
                        self.typing("'Do you need more information on any others. Over'")
                    # Interact action.
                    elif response == "INTERACT":
                        self.typing("'Coastguard. If you have an item in you bag. Break")
                        self.typing("'And you think you can use it with another item. Break'")
                        self.typing("'Or you need to enter a code or something. Break")
                        self.typing("'It needs a subject ie. Interact Ball / I Ball. Break")
                        self.typing("'And will only work if you have the bat in your bag. Break")
                        self.typing("'Do you need more information on any others. Over")
                    # Open action
                    elif response == "OPEN":
                        self.typing("'Coastguard. Sometimes things will be closed. Break'")
                        self.typing("'You can open them with this, if they aren't locked. Break'")
                        self.typing("'It needs a subject ie. Open Door / O Door. Break'")
                        self.typing("'Do you need more information on any others. Over'")
                    # Take action
                    elif response == "TAKE":
                        self.typing("'Coastguard. There are many movable things on The Island. Break'")
                        self.typing("'You can pick them up to put in your bag. Break'")
                        self.typing("'It needs a subject ie. Take Hat / T Hat. Break'")
                        self.typing("'Do you need more information on any others. Over'")
                    # Drop action
                    elif response == "DROP":
                        self.typing("'Coastguard. If you need to make room in your bag. Break'")
                        self.typing("'Drop a item. It will remain there if you want it again. Break'")
                        self.typing("'It needs a subject ie. Drop Hat / D Hat. Break'")
                        self.typing("'Do you need more information on any others. Over'")
                    # Talk action
                    elif response == "SPEAK":
                        self.typing("'Coastguard. I hear there are other being on The Island. Break'")
                        self.typing("'They may be able to help you, so talk to them. Break'")
                        self.typing("'It needs a subject ie. Speak Pirate / S Pirate. Break'")
                        self.typing("'Do you need more information on any others. Over'")
                    # Consume action
                    elif response == "EAT":
                        self.typing("'Coastguard. You lose energy and hydration as you move. Break'")
                        self.typing("'Eat and drink edible items to replenish this . Break'")
                        self.typing("'It needs a subject ie. Eat Apple / E Apple. Break'")
                        self.typing("'Do you need more information on any others. Over'")
                    # None to break the help for actions.
                    elif response == "NO":
                        self.typing("'Coastguard. Roger. Anything else I can help you with. Over'")
                        break
                    # Any other response.
                    else:
                        # Invalid
                        self.typing(f"'Coastguard. You are broken and unreadable. Say again. Over'")
            # No longer require help.
            elif response == "NOTHING":
                # Break help loop
                self.typing(f"'Coastguard. Roger. Out'")
                break
            # Did not enter a valid response.
            else:
                # Invalid response.
                self.typing(f"'Coastguard. You are broken and unreadable. Say again. Over'")

    def clear_page_and_redisplay_information(self):
        """
        If the player wants to refresh the page, back to when they arrived in the location, with the changes they have made.
        """
        self.clear_screen()
        self.show_location_items_information()
        self.show_energy_and_hydration_information()
        self.show_options_for_movement()

    def display_bag_contents(self):
        """
        Show how many spots in the bag are taken up and what's in the bag.
        """
        print(self.backpack.list())

    def display_chart(self):
        """
        Show the chart so the player can get a sense of where they are.
        """
        print(self.chart.show_chart())

    def quit_game_option(self):
        """
        Quit the game, but they can start again.
        """
        while True:
            print("Are you sure you want to quit the game? (Yes / No)")
            quit_game = input("- ").strip().upper()
            # Yes, quit game.
            if quit_game == "YES":
                self.quit_end = True
                self.moved = True
                break
            # No, keep playing.
            elif quit_game == "NO":
                break
            # Any other input.
            else:
                print("\nYou must confirm either Yes or No.")

    def look_at_an_item(self):
        """
        If the player wants more information on an item.
        """
        # Is the noun an item?
        if self.current_input_noun in [item.get_name() for item in self.game_items]:
            # Is the noun located in the current location?
            if self.current_input_noun in [item.get_name() for item in self.current_location.get_location_items()]:
                # Find the item.
                for item in self.current_location.get_location_items():
                    if item.get_name() == self.current_input_noun:
                        # Is visible.
                        if item.get_visibility_status():
                            if isinstance(item, Consumable):
                                if self.ability == "INTELLIGENCE":
                                    print(item.intelligent_inspect())
                                else:
                                    print(item.inspect())
                            else:
                                print(item.inspect())
                        # Not visible yet.
                        else:
                            print(f"{self.current_input_noun} can't be seen in this location yet.")
            # Is the noun located in the players bag?
            elif self.current_input_noun in [item.get_name() for item in self.backpack.items()]:
                # Find the item.
                for item in self.backpack.items():
                    if item.get_name() == self.current_input_noun:
                        # Inspect it.
                        print(item.inspect())
            # The noun isn't located in the current location or the players bag.
            else:
                print(f"{self.current_input_noun} isn't located here or in your bag.")
        # The noun isn't a valid item to inspect.
        else:
            print(f"{self.current_input_noun} is not a valid item to {self.current_input_action}.")

    def move_to_a_new_location(self):
        """
        If the player wants to move to a different location.
        """
        # To move to the location to the North.
        if self.current_input_noun == "NORTH" or self.current_input_noun == "N":
            # Movement is true and add one to move tally.
            self.moved = True
            self.moves += 1
            # If North goes to sea location and death.
            if type(self.game_locations[self.current_location.get_north_id()]) is SeaLocation:
                while True:
                    print(f"Please confirm the move, as "
                          f"{self.game_locations[self.current_location.get_north_id()].get_cardinal_description_text()} "
                          f"(Yes / No)")
                    confirm = input("- ").strip().upper()
                    if confirm == "YES":
                        self.clear_screen()
                        print(self.game_locations[self.current_location.get_north_id()].get_location_description_text())
                        self.ocean_death_end = True
                        break
                    elif confirm == "NO":
                        break
                    else:
                        print("\nYou must confirm either Yes or No.")
            # If North goes to an explorable location.
            else:
                self.chart.remove_player_location(self.current_location)
                self.current_location_index = self.current_location.get_north_id()
                self.current_location = self.game_locations[self.current_location_index]

        # To move to the location to the East.
        elif self.current_input_noun == "EAST" or self.current_input_noun == "E":
            # Movement is true and add one to move tally.
            self.moved = True
            self.moves += 1
            # If East goes to sea location and death.
            if type(self.game_locations[self.current_location.get_east_id()]) is SeaLocation:
                while True:
                    print(f"Please confirm the move, as "
                          f"{self.game_locations[self.current_location.get_east_id()].get_cardinal_description_text()} "
                          f"(Yes / No)")
                    confirm = input("- ").strip().upper()
                    if confirm == "YES":
                        self.clear_screen()
                        print(self.game_locations[self.current_location.get_east_id()].get_location_description_text())
                        self.ocean_death_end = True
                        break
                    elif confirm == "NO":
                        break
                    else:
                        print("\nYou must confirm either Yes or No.")

            # If East goes to an explorable location.
            else:
                self.chart.remove_player_location(self.current_location)
                self.current_location_index = self.current_location.get_east_id()
                self.current_location = self.game_locations[self.current_location_index]

        # To move to the location to the South.
        elif self.current_input_noun == "SOUTH" or self.current_input_noun == "S":
            # Movement is true and add one to move tally.
            self.moved = True
            self.moves += 1
            # If South goes to sea location and death.
            if type(self.game_locations[self.current_location.get_south_id()]) is SeaLocation:
                while True:
                    print(f"Please confirm the move, as "
                          f"{self.game_locations[self.current_location.get_south_id()].get_cardinal_description_text()} "
                          f"(Yes / No)")
                    confirm = input("- ").strip().upper()
                    if confirm == "YES":
                        self.clear_screen()
                        print(self.game_locations[self.current_location.get_south_id()].get_location_description_text())
                        self.ocean_death_end = True
                        break
                    elif confirm == "NO":
                        break
                    else:
                        print("\nYou must confirm either Yes or No.")

            # If South goes to an explorable location.
            else:
                self.chart.remove_player_location(self.current_location)
                self.current_location_index = self.current_location.get_south_id()
                self.current_location = self.game_locations[self.current_location_index]

        # To move to the location to the West.
        elif self.current_input_noun == "WEST" or self.current_input_noun == "W":
            # Movement is true and add one to move tally.
            self.moved = True
            self.moves += 1
            # If West goes to sea location and death.
            if type(self.game_locations[self.current_location.get_west_id()]) is SeaLocation:
                while True:
                    print(f"Please confirm the move, as "
                          f"{self.game_locations[self.current_location.get_west_id()].get_cardinal_description_text()} "
                          f"(Yes / No)")
                    confirm = input("- ").strip().upper()
                    if confirm == "YES":
                        self.clear_screen()
                        print(self.game_locations[self.current_location.get_west_id()].get_location_description_text())
                        self.ocean_death_end = True
                        break
                    elif confirm == "NO":
                        break
                    else:
                        print("\nYou must confirm either Yes or No.")

            # If West goes to an explorable location.
            else:
                self.chart.remove_player_location(self.current_location)
                self.current_location_index = self.current_location.get_west_id()
                self.current_location = self.game_locations[self.current_location_index]

        # Invalid noun with action MOVE.
        else:
            print(f"The input {self.current_input_noun} is not a valid direction.\n"
                  "If you want to move, please choose on of the following (North / East / South / West)")
            return

        # Minus energy and hydration.
        if self.ability == "DEXTERITY":
            if self.moves % 2 == 0:
                self.energy -= 1
                self.hydration -= 1
        else:
            self.energy -= 1
            self.hydration -= 1

        # Allow time to ready final text if moved into the ocean.
        if self.ocean_death_end:
            print("\nPress [ENTER] to continue.")
            input("- ")

        # Check enough energy and hydration for the move, or death.
        if self.energy < 0:
            print("Starvation takes hold as you try to get to the next location.\n"
                  "With no energy to continue, you close your eyes for the last time...")
            self.land_death_end = True
            print(f"\nPress [ENTER] to continue.")
            input("- ")
        elif self.hydration < 0:
            print("Dehydration takes hold as you try to get to the next location.\n"
                  "The world is spinning as you close your eyes for the last time...")
            self.land_death_end = True
            print(f"\nPress [ENTER] to continue.")
            input("- ")

    def interact_with_the_dashboard(self):
        """
        If the player wants to interact with the dashboard.
        """
        # Is the noun here?
        if self.dashboard in self.current_location.get_location_items():
            # Do you have the required item?
            if self.boat_key in self.backpack.items():
                print(self.backpack.remove(self.boat_key, self.current_location))
                print(f"{self.boat_key.get_name()} inserted!\n{self.dashboard.get_key_true_text()}")
                self.dashboard.key_inserted()
                # Removes item from the game.
                self.current_location.remove_location_item(self.boat_key)
            # Do you have the required items?
            elif self.tension_rod in self.backpack.items() and self.key_rake in self.backpack.items():
                print(f"{self.tension_rod.get_name()} applies the force!\n"
                      f"{self.key_rake.get_name()} depresses the pins!\n"
                      f"{self.dashboard.get_key_true_text()}")
                self.dashboard.key_inserted()
                # Removes items from the game.
                self.backpack.remove(self.tension_rod, self.current_location)
                self.backpack.remove(self.key_rake, self.current_location)
                self.current_location.remove_location_item(self.key_rake)
                self.current_location.remove_location_item(self.tension_rod)
            # Doesn't have the required item.
            else:
                print("I don't have any way to turn the key chamber in my bag...")
        # Wrong location.
        else:
            # Invalid
            print(f"The is no {self.current_input_noun} here.")

    def interact_with_the_compartment(self):
        """
        If the player wants to interact with the compartment.
        """
        # Is the noun here?
        if self.compartment in self.current_location.get_location_items():
            # Do you have the required item?
            if self.battery in self.backpack.items():
                print(f"{self.backpack.remove(self.battery, self.current_location)}")
                print(f"{self.battery.get_name()} inserted!\n"
                      f"{self.compartment.get_battery_true_text()}")
                self.compartment.battery_inserted()
                self.dashboard.dashboard_powered()
                # Removes item from the game.
                self.current_location.remove_location_item(self.battery)
            # Do you have the required item?
            elif self.cable in self.backpack.items():
                self.compartment.cable_inserted()
                print(f"{self.cable.get_name()} plugged in!\n"
                      f"{self.compartment.get_cable_true_text()}")
                # If the cable is plugged into the metal box.
                if self.metal_box.get_insert_status():
                    print(f"{self.backpack.remove(self.cable, self.current_location)}")
                    self.dashboard.dashboard_powered()
                    # Removes item from the game.
                    self.backpack.remove(self.cable, self.current_location)
                    self.current_location.remove_location_item(self.cable)
                # Hint they need to do that.
                else:
                    print(f"Now to find somewhere to plug other other end...")
            # Doesn't have the required item.
            else:
                print("I don't have any way to supply power in my bag...")
        # Wrong location.
        else:
            print(f"The is no {self.current_input_noun} here.")

    def interact_with_the_fuel_tank(self):
        """
        If the player wants to interact with the fuel tank.
        """
        # Is the noun here?
        if self.fuel_tank in self.current_location.get_location_items():
            # Do you have the required item?
            if self.jerry in self.backpack.items():
                self.dashboard.boat_fueled()
                print(self.backpack.remove(self.jerry, self.current_location))
                self.fuel_tank.item_inserted()
                print(f"{self.jerry.get_name()} emptied into the fuel tank.\n"
                      f"{self.fuel_tank.get_full_text()}")
                # Removes item from the game.
                self.current_location.remove_location_item(self.jerry)
            # Do you have the required item?
            elif self.alcohol in self.backpack.items():
                self.dashboard.boat_fueled()
                print(self.backpack.remove(self.alcohol, self.current_location))
                self.fuel_tank.item_inserted()
                print(f"{self.alcohol.get_name()} emptied into the fuel tank.\n"
                      f"{self.fuel_tank.get_full_text()}")
                # Removes item from the game.

                self.current_location.remove_location_item(self.alcohol)
            # Doesn't have the required item.
            else:
                print(f"I need something to fill the tank with...")
        # Wrong location.
        else:
            print(f"The is no {self.current_input_noun} here.")

    def interact_with_the_keypad(self):
        """
        If the player wants to interact with the keypad.
        """
        # Is the noun here?
        if self.keypad in self.current_location.get_location_items():
            # Is it visible?
            if self.keypad.get_visibility_status():
                print("Please enter the 4 digit code.")
                input_code = input("- ").upper().strip()
                if input_code == self.keypad.get_access_code():
                    print(self.heavy_chest.unlock_container())
                else:
                    print(f"{self.heavy_chest.get_name()} remains locked.")
            # Invalid.
            else:
                print(f"{self.current_input_noun} can't be seen in this location... yet.")
        # Invalid.
        else:
            print(f"The is no {self.current_input_noun} here.")

    def interact_with_the_button(self):
        """
        If the player wants to interact with the button.
        """
        # Is the noun here?
        if self.button in self.current_location.get_location_items():
            # All conditions met to start boat.
            if self.dashboard.get_key_status() and self.dashboard.get_power_status() and self.dashboard.get_fuel_status():
                print("The boat engine roars to life as you cast off the rope.")
                self.moved = True
                self.boat_end = True
                print("\nPress [ENTER] to continue.")
                input("- ")
            else:
                print("Nothing happens...")
        # Wrong location.
        else:
            print(f"The is no {self.current_input_noun} here.")

    def interact_with_the_metal_box(self):
        """
        If the player wants to interact with the metal box.
        """
        # Is the noun here?
        if self.metal_box in self.current_location.get_location_items():
            # Do you have the required item?
            if self.cable in self.backpack.items():
                self.metal_box.item_inserted()
                print(f"{self.cable.get_name()} plugged in.\n{self.metal_box.get_full_text()}")
                # If the cable is plugged in at the other end.
                if self.compartment.get_cable_status():
                    self.dashboard.dashboard_powered()
                    # Removes item from the game.
                    self.backpack.remove(self.cable, self.current_location)
                    self.current_location.remove_location_item(self.cable)
                # Hint to find other place to plug in
                else:
                    print(f"Now to find somewhere to plug in other other end...")
            # Doesn't have the required item.
            else:
                print(f"I need to find something to plug in here...")
        # Wrong location.
        else:
            print(f"The is no {self.current_input_noun} here.")

    def interact_with_the_coconut(self):
        """
        If the player wants to interact with the coconut.
        """
        # Is the noun here?
        if self.coconut in self.current_location.get_location_items():
            # Is it visible?
            if self.coconut.get_visibility_status():
                # Do you have the required item?
                if self.rock in self.backpack.items():
                    print(f"A perfect hit.\n{self.coconut.get_coconut_ground_text()}")
                    self.palm.item_one_taken()
                    self.coconut.condition_met()
                    self.coconut.set_location_description_text(self.coconut.get_coconut_ground_text())
                    # Removes item from the game.
                    self.backpack.remove(self.rock, self.current_location)
                    self.current_location.remove_location_item(self.rock)
                # Hint
                else:
                    print(
                        "The COCONUT is out of reach.\n"
                        "You need something to throw at it...")
            # Not visible.
            else:
                print(f"{self.current_input_noun} can't be seen in this location yet.")
        # Wrong location.
        else:
            print(f"The is no {self.current_input_noun} here.")

    def interact_with_the_sand(self):
        """
        If the player wants to interact with the sand.
        """
        # Is the noun here?
        if self.sand in self.current_location.get_location_items():
            # Do you have the required item?
            if self.shovel in self.backpack.items():
                self.sand.condition_met()
                print("You begin to dig with your shovel...")
                time.sleep(2)
                print(f"What have we here.\n{self.sand.get_reveal_text()}")
                revealed_item = self.sand.get_revealed_item()
                revealed_item.make_visible()
                revealed_item.item_discovered()
                # Removes item from the game.
                self.backpack.remove(self.shovel, self.current_location)
                self.current_location.remove_location_item(self.shovel)
            # Hint
            else:
                print("The sharp shells cut your hands.\nYou need something to dig with...")
        # Wrong location.
        else:
            print(f"The is no {self.current_input_noun} here.")

    def interact_with_the_block(self):
        """
        If the player wants to interact with the block.
        """
        # Is the noun here?
        if self.block in self.current_location.get_location_items():
            # Get numbered blocks in bag.
            numbered_blocks = []
            numbered_blocks_string = ""
            for item in self.backpack.items():
                if item.get_name().startswith("BLOCK"):
                    numbered_blocks.append(item)
            if len(numbered_blocks) == 0 and all(
                    slot is None for slot in self.block.list_slot_items()):
                print("You don't have any granite blocks to insert.\n"
                      "There are no granite blocks inserted for you to take.")
            else:
                for numbered_block in numbered_blocks:
                    numbered_blocks_string += f"{numbered_block.get_name().split()[1]} / "

                # Get available and occupied slots.
                slots = self.block.list_slot_items()
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
                        slot is not None for slot in self.block.list_slot_items()):
                    interact_options_string = "Insert / Take / "
                elif len(numbered_blocks) > 0 and all(
                        slot is None for slot in self.block.list_slot_items()):
                    interact_options_string = "Insert / "
                elif len(numbered_blocks) == 0 and any(
                        slot is not None for slot in self.block.list_slot_items()):
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
                        if numbered_block_choice in [numbered_block.get_name().split()[1] for numbered_block in
                                                     numbered_blocks]:
                            for numbered_block in numbered_blocks:
                                if numbered_block_choice == numbered_block.get_name().split()[1]:
                                    # Insert into slot 1.
                                    if slot_choice == "1" and self.block.get_slot_one_item() is None:
                                        print(f"\n{self.backpack.remove(numbered_block, self.current_location)}")
                                        self.current_location.remove_location_item(numbered_block)
                                        self.block.set_slot_one_item(numbered_block)
                                        print(f"Slot 1 now contains {numbered_block.get_name()}")
                                    # Insert into slot 2.
                                    elif slot_choice == "2" and self.block.get_slot_two_item() is None:
                                        print(f"\n{self.backpack.remove(numbered_block, self.current_location)}")
                                        self.current_location.remove_location_item(numbered_block)
                                        self.block.set_slot_two_item(numbered_block)
                                        print(f"Slot 2 now contains {numbered_block.get_name()}")
                                    # Insert into slot 3.
                                    elif slot_choice == "3" and self.block.get_slot_three_item() is None:
                                        print(f"\n{self.backpack.remove(numbered_block, self.current_location)}")
                                        self.current_location.remove_location_item(numbered_block)
                                        self.block.set_slot_three_item(numbered_block)
                                        print(f"Slot 3 now contains {numbered_block.get_name()}")
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
                    if self.block.get_slot_one_item() == self.block_six and \
                            self.block.get_slot_two_item() == self.block_zero and \
                            self.block.get_slot_three_item() == self.block_five:
                        print("\nWell that's all the slots filled...")
                        print(f"{self.block.get_slot_items()}")
                        time.sleep(2)
                        # Complete puzzle and game. Break loop.
                        print("\nA giant tentacle pulls you forward and over the cliff.\n"
                              "It holds you just above the water.\n"
                              "In your head you hear a voice...\n"
                              "You have solved the puzzle, so shall help you.\n"
                              "I know where you need to go, I've been watching them too.\n"
                              "You move around The Island and to the South in the Krakens grasp.")
                        self.kraken_end = True
                        self.moved = True
                        print("\nPress [ENTER] to continue.")
                        input("- ")
                    # If three blocks inserted and incorrect.
                    elif all(slot is not None for slot in self.block.list_slot_items()):
                        # Still has attempts left.
                        if self.kraken_block_attempts < 2:

                            print("\nWell that's all the slots filled...")
                            print(f"{self.block.get_slot_items()}")
                            time.sleep(2)
                            print("The water in front of you explodes")
                            print("I giant tentacle knocks you back onto the flat plain.")
                            self.kraken_block_attempts += 1
                            self.moved = True
                            self.chart.remove_player_location(self.current_location)
                            self.current_location_index = self.current_location.get_south_id()
                            self.current_location = self.game_locations[self.current_location_index]
                            self.location_eight.add_item_to_location(self.block.get_slot_one_item())
                            self.location_eight.add_item_to_location(self.block.get_slot_two_item())
                            self.location_eight.add_item_to_location(self.block.get_slot_three_item())
                            self.block.set_slot_one_item(None)
                            self.block.set_slot_two_item(None)
                            self.block.set_slot_three_item(None)
                            print("The blocks you had previously inserted land around you.")
                            print("\nPress [ENTER] to continue.")
                            input("- ")
                        # Too many attempts and lose game.
                        else:
                            print("\nWell that's all the slots filled...")
                            print(f"{self.block.get_slot_items()}")
                            time.sleep(2)
                            print("The water in front of you explodes.\n"
                                  "This time the giant tentacle pulls you forward.\n"
                                  "You're plunged into the endless abyss below the cliff.\n"
                                  "Descending fast, the light soon disappears.\n"
                                  "You lose consciousness surrounded by darkness...")
                            self.ocean_death_end = True
                            print("\nPress [ENTER] to continue.")
                            input("- ")
                # Take
                elif action_choice == "TAKE" and any(slot is not None for slot in self.block.list_slot_items()):
                    # Slot option
                    print(f"\n{self.block.get_slot_items()}")
                    print(f"Which slot do you want to take a BLOCK from? {occupied_slots_string}Leave)")
                    take_choice = input("- ").upper().strip()
                    # From slot 1.
                    if take_choice == "1" and self.block.get_slot_one_item() is not None:
                        print(f"\n{self.backpack.add(self.block.get_slot_one_item())}")
                        self.block.set_slot_one_item(None)
                        print(f"Slot 1 is now empty")
                    # From slot 2.
                    elif take_choice == "2" and self.block.get_slot_two_item() is not None:
                        print(f"\n{self.backpack.add(self.block.get_slot_two_item())}")
                        self.block.set_slot_two_item(None)
                        print(f"Slot 2 is now empty")
                    # From slot 3.
                    elif take_choice == "3" and self.block.get_slot_three_item() is not None:
                        print(f"\n{self.backpack.add(self.block.get_slot_three_item())}")
                        self.block.set_slot_three_item(None)
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
            print(f"The is no {self.current_input_noun} here.")

    def open_an_item(self):
        """
        If the player wants to open a container to reveal what's inside. Must be unlocked.
        """
        # Is the noun an item.
        if self.current_input_noun in [item.get_name() for item in self.game_items]:
            # Is the noun here?
            if self.current_input_noun in [item.get_name() for item in self.current_location.get_location_items()]:
                # Is noun a container?
                container = None
                for item in self.game_items:
                    if item.get_name() == self.current_input_noun:
                        container = item
                if isinstance(container, Container):
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
                    print(f"{self.current_input_noun} cannot be opened.")
            # Invalid.
            else:
                print(f"There is no {self.current_input_noun} here.")
        # Invalid.
        else:
            print(f"{self.current_input_noun} is not a valid item.")

    def take_an_item_and_put_it_in_the_players_bag(self):
        """
        If the player wants to take an item to put in their bag. They can use it at a later stage.
        """
        # Is the noun an item?
        if self.current_input_noun in [item.get_name() for item in self.game_items]:
            # Is the subject located in the current location?
            if self.current_input_noun in [item.get_name() for item in self.current_location.get_location_items()]:
                # Find the item.
                for item in self.current_location.get_location_items():
                    if item.get_name() == self.current_input_noun:
                        # If item is visible.
                        if item.get_visibility_status():
                            # Is it movable.
                            if isinstance(item, Movable):
                                if self.backpack.count() < self.backpack.get_capacity():
                                    # If getting the item has a condition to meet before being taken.
                                    if isinstance(item, Conditional):
                                        if item.get_condition_status():
                                            # Add it to your bag.
                                            print(self.backpack.add(item))
                                            self.current_location.remove_location_item(item)
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
                                        if self.water_bottle in self.backpack.items():
                                            # If the water bottle is already full.
                                            if self.water_bottle.get_water_bottle_status():
                                                print("The water bottle is already full.")
                                            # If the water bottle is empty.
                                            else:
                                                # Fill up the water bottle.
                                                print(self.water_bottle.fill_water_bottle())
                                        # No water bottle.
                                        else:
                                            # Give clue.
                                            print("I can't just put water in my bag...\n"
                                                  "If only I had a water bottle.")
                                    # Take the item.
                                    else:
                                        # Add it to your bag.
                                        print(self.backpack.add(item))
                                        self.current_location.remove_location_item(item)
                                        # If it was revealed by another item.
                                        if isinstance(item, RevealedMovable) or \
                                                isinstance(item, RevealedConsumable):
                                            taken_from = item.get_item_revealed_by()
                                            taken_from.item_one_taken()
                                            if isinstance(item, DualRevealsMovable):
                                                taken_from.item_two_taken()
                                else:
                                    print("Your bag is full. Drop an item first.")
                            else:
                                print(f"{self.current_input_noun} can't be taken.")
                        else:
                            print(f"{self.current_input_noun} can't be seen in this location yet.")
            # The noun isn't located in the current location
            else:
                # Invalid response.
                print(f"{self.current_input_noun} isn't located here.")
        # The noun isn't a valid item to take.
        else:
            # Invalid
            print(f"{self.current_input_noun} is not a valid item.")

    def drop_something_from_the_players_bag(self):
        """
        If the player wants to  drop something from their bag. Item will remain on the ground where they dropped it.
        """
        # Is the noun an item?
        if self.current_input_noun in [item.get_name() for item in self.game_items]:
            # Is the noun in the bag?
            if self.current_input_noun in [item.get_name() for item in self.backpack.items()]:
                # Find item.
                for item in self.backpack.items():
                    if self.current_input_noun == item.get_name():
                        # Remove it and drop it in the current location.
                        print(self.backpack.remove(item, self.current_location))
                        print("It now lies on the ground.")
            # Invalid
            else:
                print(f"You aren't carrying a {self.current_input_noun} in your bag to drop.")
        # Invalid.
        else:
            print(f"{self.current_input_noun} is not a valid item.")

    def speak_with_merman(self):
        """
        If the player wants to speak with the merman to retrieve an item.
        """
        # Is the noun here?
        if self.merman in self.current_location.get_location_items():
            # Is it visible?
            if self.merman.get_visibility_status():
                # Initial dialogue.
                print(f"{self.merman.get_initial_dialogue()} (Yes / No)")
                response = input().upper().strip()
                # Respond yes.
                if response == "YES":
                    # Make items visible to help.
                    if self.ability == "CHARISMA":
                        self.jerry.make_visible()
                        self.cable.make_visible()
                        print("\nI can't help you escape this island, you're too weak in the water.\n"
                              "I saw some things in the water to the North though.")

                    # If items he can help get haven't been discovered.
                    if not self.jerry.get_visibility_status() and not self.cable.get_visibility_status():
                        print("\nI can't help you escape this island, you're too weak in the water.\n"
                              "If there is something else, come back and see me.")
                    # Items discovered.
                    else:
                        print("\nI could retrieve something from the water for you, but it will cost you a some gold.")
                        # Nothing in bag to trade.
                        if self.coin not in self.backpack.items() and self.trident not in self.backpack.items():
                            if self.ability == "CHARISMA":
                                print("There is a lost Trident and Coin on The Island.\n"
                                      "If you bring me either of them, I will help you.")
                            else:
                                print("Come back when you have something to trade.")
                        # Item in bag to trade.
                        else:
                            # Get items available to trade.
                            trade_items = []
                            trade_items_string = ""
                            for item in self.backpack.items():
                                if item is self.coin or item is self.trident:
                                    trade_items.append(item)
                                    trade_items_string += f"{item.get_name().capitalize()} / "

                            # Get items available to get from the ocean.
                            ocean_items = []
                            ocean_items_string = ""
                            if not self.buoy.get_item_one_taken_status():
                                ocean_items.append(self.buoy.get_revealed_item()[0])
                                ocean_items_string += f"{self.buoy.get_revealed_item()[0].get_name().capitalize()} / "
                            if not self.buoy.get_item_two_taken_status():
                                ocean_items.append(self.buoy.get_revealed_item()[1])
                                ocean_items_string += f"{self.buoy.get_revealed_item()[1].get_name().capitalize()} / "

                            # Get input.
                            print(f"What do you have to trade? ({trade_items_string[:-3]})")
                            payment = input("- ").upper().strip()
                            payment_item = None
                            # Trade coin.
                            if payment == "COIN" and self.coin in trade_items:
                                print(f"\n{self.backpack.remove(self.coin, self.current_location)}")
                                self.current_location.remove_location_item(self.coin)
                                payment_item = self.coin

                            # Trade trident.
                            elif payment == "TRIDENT" and self.trident in trade_items:
                                print(f"\n{self.backpack.remove(self.trident, self.current_location)}")
                                self.current_location.remove_location_item(self.trident)
                                payment_item = self.trident

                            # Try to trade coin but don't have it.
                            elif payment == "COIN" and self.coin not in trade_items:
                                print("\nYou don't have a coin.\nReturn when you have something.")

                            # Try to trade trident but don't have it.
                            elif payment == "TRIDENT" and self.trident not in trade_items:
                                print("\nYou don't have a trident.\nReturn when you have something.")

                            # Invalid
                            else:
                                print(f"\n{payment} is worthless to me.\nReturn when you have something better.")

                            if payment_item is not None:
                                print(f"\nWhat do you want me to retrieve for you? "
                                      f"({ocean_items_string[:-3]})")
                                response = input("- ").upper().strip()
                                # Want cable.
                                if response == "CABLE" and not self.buoy.get_item_one_taken_status():
                                    print("\nI'll be back in a minute.")
                                    time.sleep(2)
                                    print(self.backpack.add(self.cable))
                                    self.buoy.item_one_taken()
                                    self.location_six.remove_location_item(self.cable)
                                    print("Pleasure doing business with you.")
                                # Want jerry.
                                elif response == "JERRY" and not self.buoy.get_item_two_taken_status():
                                    print("\nI'll be back in a minute.")
                                    time.sleep(2)
                                    print(self.backpack.add(self.jerry))
                                    self.buoy.item_two_taken()
                                    self.location_six.remove_location_item(self.jerry)
                                    print("Pleasure doing business with you.")
                                else:
                                    print(f"\nThere isn't a {response} underwater.\nTake your {payment} back.")
                                    print(self.backpack.add(payment_item))
                # Respond no.
                elif response == "NO":
                    print("Be on your way then.")
                # Any other response.
                else:
                    print(f"{response}... Don't play games. Go away then.")
            # Invalid.
            else:
                print(f"{self.current_input_noun} isn't here anymore...")
        # Invalid.
        else:
            print(f"The is no {self.current_input_noun} here.")

    def speak_with_parrot(self):
        """
        If the player wants to speak with the parrot to retrieve an item.
        """
        # Is the noun here?
        if self.parrot in self.current_location.get_location_items():
            # If the coin is still there.
            if not self.ship.get_item_two_taken_status():
                # Do you have crackers?
                if self.crackers in self.backpack.items():
                    # Get input.
                    print(f"{self.parrot.get_initial_dialogue()}")
                    print(f"Give CRACKERS (Yes / No)")
                    response = input("- ").upper().strip()
                    # Give crackers.
                    if response == "YES":
                        print(f"\n{self.backpack.remove(self.crackers, self.current_location)}")
                        self.current_location.remove_location_item(self.crackers)
                        print("Squawk. Let me give you something in return.")
                        print("Be right back.")
                        time.sleep(2)
                        print("Here, have a gold coin.")
                        print(self.backpack.add(self.coin))
                        self.ship.item_two_taken()
                        self.location_nine.remove_location_item(self.coin)
                    # Any other response.
                    else:
                        print(f"{self.parrot.get_initial_dialogue()}")
                elif self.ability == "CHARISMA":
                    print(f"{self.parrot.get_initial_dialogue()}")
                    consumables = list()
                    consumables_string = ""
                    for item in self.backpack.items():
                        if isinstance(item, Consumable):
                            consumables.append(item)
                            consumables_string += f"{item.get_name().capitalize()} / "
                    if len(consumables) > 0:
                        print("I don't have any crackers...")
                        print(f"But I do have ({consumables_string[:-3]})")
                        give_parrot = input("- ").strip().upper()
                        given = False
                        for item in consumables:
                            if item.get_name() == give_parrot:
                                print(self.backpack.remove(item, self.current_location))
                                given = True
                                self.current_location.remove_location_item(item)
                                print("Squawk. Let me give you something in return.")
                                print("Be right back.")
                                time.sleep(2)
                                print("Here, have a gold coin.")
                                self.coin.make_visible()
                                self.coin.condition_met()
                                self.ship.item_two_taken()
                                self.location_nine.remove_location_item(self.coin)
                                print(self.backpack.add(self.coin))
                        if not given:
                            print(f"Squawk. You don't have a {give_parrot}")
                    else:
                        print("I don't have any food to give you, sorry.")

                # No crackers to give.
                else:
                    print(f"{self.parrot.get_initial_dialogue()}")
            else:
                print("Squawk. Thanks for the food.")
        # Invalid.
        else:
            print(f"The is no {self.current_input_noun} here.")

    def speak_with_kraken(self):
        """
        If the player wants to speak with the kraken to get how many chances they have left with the block.
        """
        print(f"{self.kraken.get_initial_dialogue()}\n"
              f"You have {2 - self.kraken_block_attempts} attempts left.")

    def eat_or_drink_a_consumable_item(self):
        """
        If the player wants to eat or drink something to replenish energy and hydration levels. May also subtract.
        """
        # Is the noun an item.
        if self.current_input_noun in [item.get_name() for item in self.game_items]:
            # Is the noun here?
            if self.current_input_noun in [item.get_name() for item in self.current_location.get_location_items()] or \
                    self.current_input_noun in [item.get_name() for item in self.backpack.items()]:
                # Is the noun consumable?
                consumable = None
                for item in self.game_items:
                    if item.get_name() == self.current_input_noun:
                        consumable = item
                if isinstance(consumable, Consumable):
                    # If it is visible.
                    if consumable.get_visibility_status():
                        if consumable is self.water_bottle and not self.water_bottle.get_water_bottle_status():
                            print(f"The {self.water_bottle.get_name()} is empty.")
                        else:
                            if consumable is self.water:
                                pass
                            elif consumable is self.water_bottle:
                                self.water_bottle.empty_water_bottle()
                            # If it's not water.
                            elif consumable is not self.water:
                                # Remove consumable
                                if consumable in self.current_location.get_location_items():
                                    self.current_location.remove_location_item(consumable)
                                elif consumable in self.backpack.items():
                                    self.backpack.remove(consumable, self.current_location)
                                    self.current_location.remove_location_item(consumable)

                            print(consumable.item_consumed())
                            # Apply consumable values.
                            self.energy += consumable.get_energy_value()
                            if self.energy > 10:
                                self.energy = 10
                            if self.energy < 0:
                                self.energy = -1
                            self.hydration += consumable.get_hydration_value()
                            if self.hydration > 10:
                                self.hydration = 10
                            if self.hydration < 0:
                                self.hydration = -1
                            # If the consumable had negative effects.
                            if self.energy < 0 or self.hydration < 0:
                                self.land_death_end = True
                                self.moved = True
                                print("\n")
                                print(f"\nPress [ENTER] to continue.")
                                input("- ")
                            else:
                                # New energy and hydration levels.
                                print(f"You now have enough energy for {self.energy} moves.")
                                print(f"You now have enough hydration for {self.hydration} moves.")
                    else:
                        print(f"{self.current_input_noun} can be seen... yet.")
                # Invalid.
                else:
                    print(f"{self.current_input_noun} is not consumable.")
            # Invalid.
            else:
                print(f"There is no {self.current_input_noun} here.")
        # Invalid.
        else:
            print(f"{self.current_input_noun} is not a valid item.")

    def play(self):
        """
        Cycle the gameplay until and ending is achieved or the player quits.
        """
        while not self.boat_end and not self.kraken_end and not self.ocean_death_end and not self.land_death_end and not self.quit_end:
            self.show_location_introduction_on_move()
            self.show_location_items_information()
            self.show_energy_and_hydration_information()
            self.show_options_for_movement()

            while not self.moved:
                self.get_players_input_on_what_they_want_to_do()
                if self.current_player_input[0] == "":
                    print("You did not enter anything.")

                elif len(self.current_player_input) == 1:
                    if self.current_player_input[0] == "HELP" or self.current_player_input[0] == "H":
                        self.player_needs_help()
                    elif self.current_player_input[0] == "REFRESH" or self.current_player_input[0] == "R":
                        self.clear_page_and_redisplay_information()
                    elif self.current_player_input[0] == "BAG" or self.current_player_input[0] == "B":
                        self.display_bag_contents()
                    elif self.current_player_input[0] == "CHART" or self.current_player_input[0] == "C":
                        self.display_chart()
                    elif self.current_player_input[0] == "QUIT" or self.current_player_input[0] == "Q":
                        self.quit_game_option()
                    else:
                        print(f"{self.current_player_input[0].capitalize()} isn't a valid one keyword command.")

                elif len(self.current_player_input) > 1:
                    # Split into the action they want to do.
                    self.current_input_action = self.current_player_input[0]
                    # And the noun to do it upon.
                    self.current_input_noun = self.current_player_input[1]
                    # If the player wants to look closer at something.
                    if self.current_input_action == "LOOK" or self.current_input_action == "L":
                        self.look_at_an_item()
                    # If the player wants to move to another location.
                    elif self.current_input_action == "MOVE" or self.current_input_action == "M":
                        self.move_to_a_new_location()
                    # If the player wants to interact with something.
                    elif self.current_input_action == "INTERACT" or self.current_input_action == "I":
                        if self.current_input_noun == "DASHBOARD":
                            self.interact_with_the_dashboard()
                        elif self.current_input_noun == "COMPARTMENT":
                            self.interact_with_the_compartment()
                        elif self.current_input_noun == "FUEL TANK":
                            self.interact_with_the_fuel_tank()
                        elif self.current_input_noun == "KEYPAD":
                            self.interact_with_the_keypad()
                        elif self.current_input_noun == "BUTTON":
                            self.interact_with_the_button()
                        elif self.current_input_noun == "METAL BOX":
                            self.interact_with_the_metal_box()
                        elif self.current_input_noun == "COCONUT":
                            self.interact_with_the_coconut()
                        elif self.current_input_noun == "SAND":
                            self.interact_with_the_sand()
                        elif self.current_input_noun == "BLOCK":
                            self.interact_with_the_block()
                        else:
                            # Is the noun here?
                            if self.current_input_noun in [item.get_name() for item in
                                                           self.current_location.get_location_items()]:
                                print(f"{self.current_input_noun} is not a valid item to Interact with.")
                            # Invalid.
                            else:
                                print(f"The is no {self.current_input_noun} here.")

                    # If the player wants to open something.
                    elif self.current_input_action == "OPEN" or self.current_input_action == "O":
                        self.open_an_item()
                    # If the player wants to take something and put it in their bag.
                    elif self.current_input_action == "TAKE" or self.current_input_action == "T":
                        self.take_an_item_and_put_it_in_the_players_bag()
                    # If the player wants to drop something from their bag.
                    elif self.current_input_action == "DROP" or self.current_input_action == "D":
                        self.drop_something_from_the_players_bag()
                    # If the player wants to speak to a NPC.
                    elif self.current_input_action == "SPEAK" or self.current_input_action == "S":
                        if self.current_input_noun == "MERMAN":
                            self.speak_with_merman()
                        elif self.current_input_noun == "PARROT":
                            self.speak_with_parrot()
                        elif self.current_input_noun == "KRAKEN":
                            self.speak_with_kraken()
                        else:
                            # Is the noun here?
                            if self.current_input_noun in [item.get_name() for item in
                                                           self.current_location.get_location_items()]:
                                print(f"{self.current_input_noun} can't talk")
                            # Invalid.
                            else:
                                print(f"The is no {self.current_input_noun} here.")

                    # If the player wants to consume something.
                    elif self.current_input_action == "EAT" or self.current_input_action == "E":
                        self.eat_or_drink_a_consumable_item()
                    # Invalid action.
                    else:
                        print(f"{self.current_input_action} is not a valid action to use with a CAPITALIZED NOUN.")

    def check_and_display_boat_end(self):
        """
        If the boat end it true.
        """
        # Complete game by taking boat.
        if self.boat_end:
            self.clear_screen()
            self.typing(f"'Coastguard. This is {self.player_name}. Are you receiving. Over'")
            self.typing(f"'{self.player_name}. This is Coastguard. Receiving. Over'")
            self.typing(f"'{self.player_name}. I have found a boat and got it started. Break'")
            self.typing("'Making my way to your position now. Over'")
            self.typing("'Coastguard. Glad to hear it. We'll be waiting. Over'")
            self.typing(f"'{self.player_name}. Roger. Out'")
            print(f"\nCongratulations {self.player_name}. You have successfully made it off The Island.")

    def check_and_display_kraken_end(self):
        """
        If the kraken end it true.
        """
        # Complete game by taking kraken.
        if self.kraken_end:
            self.clear_screen()
            self.typing(f"'Coastguard. This is {self.player_name}. Are you receiving. Over'")
            self.typing(f"'{self.player_name}. This is Coastguard. Receiving. Over'")
            self.typing(f"'{self.player_name}. Making my way to your position now. Break'")
            self.typing("'I'm coming by alternate means, do not engage. Over'")
            self.typing("'Coastguard. Acknowledged. We'll see you soon. Over'")
            self.typing(f"'{self.player_name}. Roger. Out'")
            print(f"\nCongratulations {self.player_name}. You have successfully made it off The Island.")

    def check_and_display_ocean_death_end(self):
        """
        If the ocean death end it true.
        """
        # Lose game by dying in the ocean.
        if self.ocean_death_end:
            self.clear_screen()
            self.typing("'Zero Alpha. This is Coastguard. Are you receiving. Over'")
            self.typing("'Coastguard. This is Zero Alpha. Receiving. Over'")
            self.typing(f"'Coastguard. We have {self.player_name}. Well what's left of them. Break'")
            self.typing("'Their body floated past while we were waiting. Over'")
            self.typing("'Zero Alpha. Acknowledged. You're clear to return to base. Over'")
            self.typing("'Coastguard. Roger. Out'")
            print(f"\nGAME OVER {self.player_name}. You didn't make it off The Island alive.")

    def check_and_display_land_death_end(self):
        """
        If the land death end it true.
        """
        # Lose game by dying on land.
        if self.land_death_end:
            self.clear_screen()
            self.typing("'Zero Alpha. This is Coastguard. Are you receiving. Over'")
            self.typing("'Coastguard. This is Zero Alpha. Receiving. Over'")
            self.typing("'Coastguard. Seeking permission to return to base. Break'")
            self.typing("'We have been waiting here a week. Break'")
            self.typing(f"'{self.player_name} must have perished on The Island. Over'")
            self.typing("'Zero Alpha. Acknowledged. You're clear to return to base. Over'")
            self.typing("'Coastguard. Roger. Out'")
            print(f"\nGAME OVER {self.player_name}. You didn't make it off The Island alive.")

    def check_and_display_quit_end(self):
        """
        If the player quit.
        """
        # Quit the game.
        if self.quit_end:
            self.clear_screen()
            print(f"GAME OVER {self.player_name}. You quit the game.")

    def check_play_again(self):
        """
        Gives the player a choice to play again.
        """
        while True:
            print(f"\n{self.player_name}, do you want to play again? (Yes / No)")
            play_again_input = input("- ").strip().upper()
            if play_again_input == "YES":
                return True
            elif play_again_input == "NO":
                return False
            else:
                print("\nYou must confirm either Yes or No.")

    def exit_game(self):
        """
        Final sign off if the player no longer wants to play.
        """
        print(f"\nThanks for playing {self.player_name}.\nCome back and adventure on The Island again soon.")

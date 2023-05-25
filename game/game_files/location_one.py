from random import randint
from game.classes.location import *
from game.classes.item import *
from game.game_files.location_zero import original_keypad

original_location_one = ExplorableLocation(1, 732, "GRANITE SIGN", 4, 2, 0, 13,
                                           "there is a sandy beach with a jetty.",
                                           "the sandy beach.\nA small wooden jetty extends into the water where the boat is tied.")

original_sign = Item(1, True,
                     "SIGN",
                     "Large rocks have been placed on the beach to form what seems to be an 'SOS' SIGN.",
                     "The rocks are large and are made of granite.\n"
                     "The corners of the letters are fairly square.\n"
                     "There are a few extra rocks to the bottom left.")

original_paper = Item(1, True,
                      "PAPER",
                      "Attached to the jetty is a piece of PAPER.",
                      "")

original_metal_box = RequiresInsert(1, True,
                                    "METAL BOX",
                                    "At the start of the jetty there is a METAL BOX on one of the posts.",
                                    "What looks to be an electrical box as there is a power socket inside.\n"
                                    "You could interact to insert something, if you have the right item...",
                                    "A cable is plugged into the socket in the electrical box.")

original_block_one = Movable(1, True,
                             "BLOCK 1",
                             "Near the start of the jetty lies hexagonal BLOCK 1.",
                             "A hexagonal shaped rock, made of granite. The number one is engraved on it.")

from game.classes.location import *
from game.classes.item import *

original_location_eight = ExplorableLocation(8, 552, "FLAT PLAIN", 10, 9, 5, 7,
                                             "there is a large area of flat, smooth rock.",
                                             "the flat area.\nThe rock almost seems polished smooth.")

original_trident = Movable(8, True,
                           "TRIDENT",
                           "In the middle of the area is a golden TRIDENT.",
                           "Made of solid gold, it has three prongs on one end.", )

original_sword = Movable(8, True,
                         "SWORD",
                         "Glinting in the sun is a SWORD.",
                         "The blade is shiny and as sharp as a razor.")

original_shovel = Movable(8, True,
                          "SHOVEL",
                          "Among some seaweed is a SHOVEL.",
                          "A standard shovel for digging, with a long wooden handle.")

original_block_eight = Movable(8, True,
                               "BLOCK 8",
                               "In a puddle of water lies hexagonal BLOCK 8.",
                               "A hexagonal shaped rock, made of granite. The number eight is engraved on it.")

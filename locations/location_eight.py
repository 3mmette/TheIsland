from location import *
from item import *

loc_eight = ExplorableLocation(8, 10, 9, 5, 7,
                               "there is a large area of flat, smooth rock.",
                               "the flat area.\nThe rock almost seems polished smooth.")

trident = Movable(8, True,
                  "TRIDENT",
                  "In the middle of the area is a golden TRIDENT.",
                  "Made of solid gold, it has three prongs on one end.",
                  "On the ground lies the dropped TRIDENT.")

sword = Movable(8, True,
                "SWORD",
                "Glinting in the sun is a SWORD.",
                "The blade is shiny as sharp as a razor.",
                "On the ground lies the dropped SWORD.")

shovel = Movable(8, True,
                 "SHOVEL",
                 "Among some seaweed is a SHOVEL.",
                 "A standard shovel, with a long wooden handle.",
                 "On the ground lies the dropped SHOVEL.")

hex81 = Movable(8, True,
                "BLOCK EIGHT",
                "In a puddle of water lies hexagonal BLOCK EIGHT.",
                "A hexagonal shaped rock, made of granite. The number eight is engraved on it.",
                "On the ground lies the dropped hexagonal BLOCK EIGHT.")

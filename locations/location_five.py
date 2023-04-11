from location import *
from item import *

loc_five = ExplorableLocation(5, 8, 6, 2, 4,
                              "there is a hill rising in front of you.",
                              "the top of the hill.\nThere is a crater in the centre and the ground feels warm.")

key_rake = Movable(5, False,
                   "KEY RAKE",
                   "Stuck into the side of the TREE is a KEY RAKE.",
                   "A rake that can be used to depress pins in a key chamber.")

hex51 = Movable(5, True,
                "BLOCK FIVE",
                "In the centre of the crater lies hexagonal BLOCK FIVE.",
                "A hexagonal shaped rock, made of granite. The number five is engraved on it.")

tree = Reveal(5, True, key_rake, True,
              "TREE",
              "On the side of the crater is a large dead TREE.",
              "The dead limbs stretch up towards the sky. Stuck in the truck is a KEY RAKE.",
              "The dead limbs stretch up towards the sky, creating a beautiful silhouette.")

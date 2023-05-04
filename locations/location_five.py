from classes.location import *
from classes.item import *

loc_five = ExplorableLocation(5, 615, "CRATER HILL", 8, 6, 2, 4,
                              "there is a hill rising in front of you.",
                              "the top of the hill.\nThere is a crater in the centre and the ground feels warm.")

tree = RevealsMovable(5, True, None,
                      "TREE",
                      "On the side of the crater is a large dead TREE.",
                      "The dead limbs stretch up towards the sky.",
                      "Stuck in the truck is a KEY RAKE.",
                      "It creates a beautiful silhouette.")

key_rake = RevealedMovable(5, False, tree,
                           "KEY RAKE",
                           "Stuck into the side of the tree is a KEY RAKE.",
                           "A rake that can be used to depress pins in a key chamber.")
tree.set_revealed_item(key_rake)

parrot = Npc(5, True,
             "PARROT",
             "A PARROT is sitting in the tree watching you.",
             "A green bird with a patch over one eye.\nIt squawks 'Hello'.",
             "Polly wants a cracker.")

block_five = Movable(5, True,
                     "BLOCK 5",
                     "In the centre of the crater lies hexagonal BLOCK 5.",
                     "A hexagonal shaped rock, made of granite. The number five is engraved on it.")

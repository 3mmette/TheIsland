from game.classes.location import *
from game.classes.item import *

original_location_five = ExplorableLocation(5, 654, "CRATER HILL", 8, 6, 2, 4,
                                            "there is a hill rising in front of you.",
                                            "the top of the hill.\nThere is a crater in the centre and the ground feels warm.")

original_tree = RevealsMovable(5, True, None,
                               "TREE",
                               "On the side of the crater is a large dead TREE.",
                               "The dead limbs stretch up towards the sky.",
                               "Stuck in the trunk is a KEY RAKE.",
                               "It creates a beautiful silhouette.")

original_key_rake = RevealedMovable(5, False, None,
                                    "KEY RAKE",
                                    "Stuck into the side of the tree is a KEY RAKE.",
                                    "A rake that can be used to depress pins in a key chamber.")

original_parrot = Npc(5, True,
                      "PARROT",
                      "A PARROT is sitting in the tree watching you.",
                      "A green bird with a patch over one eye.\nIt squawks 'Hello'.",
                      "Polly wants a cracker.")

original_block_five = Movable(5, True,
                              "BLOCK 5",
                              "In the centre of the crater lies hexagonal BLOCK 5.",
                              "A hexagonal shaped rock, made of granite. The number five is engraved on it.")

from game.classes.location import *
from game.classes.item import *

original_location_three = ExplorableLocation(3, 780, "SHELL BEACH", 6, 13, 13, 2,
                                             "there is a shell beach.",
                                             "the shell beach.\nSmall crabs scatter in all directions.")

original_driftwood = RevealsMovable(3, True, None,
                                    "DRIFTWOOD",
                                    "A line of DRIFTWOOD mark the high tide line.",
                                    "An assortment of wood in all shapes and sizes.",
                                    "Amongst them is a piece of metal that is a TENSION ROD.",
                                    "They are bleached white by the sun and sea.")

original_tension_rod = RevealedMovable(3, False, None,
                                       "TENSION ROD",
                                       "Amongst the driftwood lies a TENSION ROD.",
                                       "A rod that can be used to apply pressure to a key chamber.")

original_merman = Npc(3, True,
                      "MERMAN",
                      "On the shore with his tail in the water sits a MERMAN.",
                      "The top half of a God with a blue fish tail, he says 'Hello'.",
                      "What's a Human like you doing in a place like this?\nDo you need help?")

original_block_three = Movable(3, True,
                               "BLOCK 3",
                               "Contrasted against the shells lies hexagonal BLOCK 3.",
                               "A hexagonal shaped rock, made of granite. The number three is engraved on it.")

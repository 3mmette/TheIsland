from game.classes.location import *
from game.classes.item import *

loc_three = ExplorableLocation(3, 780, "SHELL BEACH", 6, 13, 13, 2,
                               "there is a shell beach.",
                               "the shell beach.\nSmall crabs scatter in all directions.")

driftwood = RevealsMovable(3, True, None,
                           "DRIFTWOOD",
                           "A line of DRIFTWOOD mark the high tide line.",
                           "An assortment of wood in all shapes and sizes.",
                           "Amongst them is a piece of metal that is a TENSION ROD.",
                           "They are bleached white by the sun and sea.")

tension_rod = RevealedMovable(3, False, driftwood,
                              "TENSION ROD",
                              "Amongst the driftwood lies a TENSION ROD.",
                              "A rod that can be used to apply pressure to a key chamber.")
driftwood.set_revealed_item(tension_rod)

merman = Npc(3, True,
             "MERMAN",
             "On the shore with his tail in the water sits a MERMAN.",
             "The top half of a God with a blue fish tail, he says 'Hello'.",
             "What's a Human like you doing in a place like this?\nDo you need help?")

block_three = Movable(3, True,
                      "BLOCK 3",
                      "Contrasted against the shells lies hexagonal BLOCK 3.",
                      "A hexagonal shaped rock, made of granite. The number three is engraved on it.")
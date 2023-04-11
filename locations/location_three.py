from location import *
from item import *

loc_three = ExplorableLocation(3, 6, 13, 13, 2,
                               "there is a shell beach.",
                               "the shell beach.\nSmall crabs scatter in all directions.")

tension_rod = Movable(3, False,
                      "TENSION ROD",
                      "Amongst the DRIFTWOOD lies a TENSION ROD.",
                      "A rod that can be used to apply pressure to a key chamber.",
                      "On the ground lies the dropped TENSION ROD")

hex31 = Movable(3, True,
                "BLOCK THREE",
                "Contrasted against the shells lies hexagonal BLOCK THREE.",
                "A hexagonal shaped rock, made of granite. The number three is engraved on it.",
                "On the ground lies the dropped hexagonal BLOCK THREE.")

driftwood = Holds(3, True, tension_rod, tension_rod,
                  "DRIFTWOOD",
                  "A line of DRIFTWOOD mark the high tide line.",
                  "Random pieces of wood, amongst them is a TENSION ROD.",
                  "Random pieces of wood, bleached white by the sun and sea.")


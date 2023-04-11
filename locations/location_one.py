from location import *
from item import *

loc_one = ExplorableLocation(1, 4, 2, 0, 13,
                             "there is a sandy beach with a jetty.",
                             "the sandy beach.\nA small wooden jetty extends into the water where the boat is tied.")

hex11 = Movable(1, True,
                "BLOCK ONE",
                "Near the start of the jetty lies hexagonal BLOCK ONE.",
                "A hexagonal shaped rock, made of granite. The number one is engraved on it.",
                "On the ground lies the dropped hexagonal BLOCK ONE.")

sign = Item(1, True,
            "SIGN",
            "Large rocks seems to have been placed on the beach to form an 'SOS' SIGN.",
            "The rocks are too large to move, and are made of granite.")

paper = Item(1, True,
             "PAPER",
             "Attached to the jetty is a piece of PAPER.",
             "Cryptic Clue...")

metal_box = Requires(1, True, ["Cable"],
                     "METAL BOX",
                     "At the start of the jetty there is a METAL BOX on one of the posts.",
                     "What looks to be an electrical box.",
                     "There is a power socket.",
                     "A cable is plugged into the socket.")

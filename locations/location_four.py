from location import *
from item import *

loc_four = ExplorableLocation(4, 7, 5, 1, 12,
                              "there is a area with a small stream.",
                              "the stream.\nThe stream runs through the area, from east to west.")

rock = Movable(4, True,
               "ROCK",
               "The bed of the stream is littered with smooth ROCK.",
               "A smooth pebble, the perfect size and weight to throw.",
               "On the ground lies the dropped ROCK")
boat_key = Movable(4, False,
                   "BOAT KEY",
                   "The BOAT KEY rests in the water near the start.",
                   "A medium sized key, with a tag that says 'For Boat'.",
                   "On the ground lies the dropped BOAT KEY")
hex41 = Movable(4, True,
                "BLOCK FOUR",
                "Under the water in the stream lies hexagonal BLOCK FOUR.",
                "A hexagonal shaped rock, made of granite. The number four is engraved on it.",
                "On the ground lies the dropped hexagonal BLOCK FOUR.")

water = "New class for this one"

spring = Reveal(4, True, boat_key, False,
                "SPRING",
                "There is a SPRING where the stream starts.",
                "At the source of the stream rests the BOAT KEY, just under the sand.",
                "Fine sand rests around where the water comes out.")

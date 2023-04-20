from location import *
from item import *

loc_four = ExplorableLocation(4, "STREAM", 7, 5, 1, 12,
                              "there is a area with a small stream.",
                              "the stream.\nThe stream runs through the area, from east to west.")

spring = ConditionalRevealsMovable(4, True, None,
                                   "SPRING",
                                   "There is a SPRING where the stream starts.",
                                   "The source of the spring is an area of fine sand.",
                                   "Just under the sand rests the BOAT KEY.",
                                   "A few small fish swim in the area.")

water = Consumable(4, True, 0, 10,
                   "WATER",
                   "The WATER makes its was down to the ocean.",
                   "It looks clean enough to drink.",
                   "Refreshing, it takes your thirst away.")

rock = Movable(4, True,
               "ROCK",
               "The bed of the stream is littered with smooth ROCK.",
               "A smooth pebble, the perfect size and weight to throw.")

boat_key = Movable(4, False,
                   "BOAT KEY",
                   "The BOAT KEY rests in the water near the start.",
                   "A medium sized key, with a tag that says 'For Boat'.")
spring._reveals_item = boat_key

block_four = Movable(4, True,
                     "BLOCK 4",
                     "Under the water in the stream lies hexagonal BLOCK 4.",
                     "A hexagonal shaped rock, made of granite. The number four is engraved on it.")

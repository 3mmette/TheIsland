from random import randint
from classes.location import *
from classes.item import *
from locations.location_zero import keypad

loc_one = ExplorableLocation(1, 687, "GRANITE SIGN", 4, 2, 0, 13,
                             "there is a sandy beach with a jetty.",
                             "the sandy beach.\nA small wooden jetty extends into the water where the boat is tied.")

sign = Item(1, True,
            "SIGN",
            "Large rocks have been placed on the beach to form what seems to be an 'SOS' SIGN.",
            "The rocks are large and are made of granite.\n"
            "The corners of the letters are fairly square.\n"
            "There are a few extra rocks to the bottom left.")

paper = Item(1, True,
             "PAPER",
             "Attached to the jetty is a piece of PAPER.",
             "")

metal_box = RequiresInsert(1, True,
                           "METAL BOX",
                           "At the start of the jetty there is a METAL BOX on one of the posts.",
                           "What looks to be an electrical box as there is a power socket inside.\n"
                           "You could interact to insert something, if you have the right item...",
                           "A cable is plugged into the socket in the electrical box.")

block_one = Movable(1, True,
                    "BLOCK 1",
                    "Near the start of the jetty lies hexagonal BLOCK 1.",
                    "A hexagonal shaped rock, made of granite. The number one is engraved on it.")

cryptic = {"ISLE": "Part of Chislehurst you can't walk away from. (4)",
           "SAND": "Hazard constructed in bricks and mortar. (4)",
           "PALM": "Handy source of coconuts. (4)",
           "SHIP": "Drink slowly, about an hour per schooner, say. (4)",
           "BOAT": "Snake on top of tea packet? (4)",
           "WAVE": "Greeting seen by the coast. (4)",
           "FISH": "Ray, for instance, is a well-known swimmer. (4)",
           "SALT": "Add some seasoning to the marsh. (4)",
           "CRAB": "Small wild apple you might find in the sea? (4)",
           "ROCK": "Music set in stone. (4)"}
cryptic_number = randint(0, 9)
count = 0
for key, value in cryptic.items():
    if count == cryptic_number:
        keypad.set_access_code(key)
        paper.set_description_text(value)
    count += 1

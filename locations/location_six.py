from location import *
from item import *
from locations.location_zero import compartment, fuel_tank
from locations.location_one import metal_box

loc_six = ExplorableLocation(6, 9, 12, 3, 5,
                             "there is a rocky shoreline.",
                             "the rocky shoreline.\nThe tide must be low as there are many things washed ashore.")

hex61 = Movable(6, True,
                "BLOCK SIX",
                "Among the things lies hexagonal BLOCK SIX.",
                "A hexagonal shaped rock, made of granite. The number six is engraved on it.")

water_bottle = WaterBottle(6, True, 0, 10,
                           "WATER BOTTLE",
                           "On the rocks lies a WATER BOTTLE.",
                           "A full bottle of natural spring water.",
                           "Refreshing, it takes your thirst away.",
                           "The water bottle is empty.")

crackers = Consumable(6, True, 5, 0,
                      "CRACKERS",
                      "On the high tide mark sits a packet of CRACKERS.",
                      "A small packet of crackers, from the company Polly.",
                      "A little dry, but still tasty.")

beans = Consumable(6, True, 5, 1,
                   "BEANS",
                   "Jammed between two rocks is a can on BEANS.",
                   "This is a tasty treat.",
                   "They may make you gassy. but they are good.")

soup = Consumable(6, True, 8, 8,
                  "SOUP",
                  "A tin of SOUP lays discarded amongst the rocks.",
                  "Hydration and calories, what more do you want.",
                  "Meat, Veg and Soup. What a great meal.")

buoy = Buoy(6, True, ['a', 'b'],
            "BUOY",
            "A BUOY floats in the water just off shore.",
            "A chain keeps in anchored to the seabed.",
            "There is a JERRY CAN of fuel near where it's anchored.",
            "The seabed below it is empty",
            "A power CABLE is tangled in the chain.",
            "The chain looks old and rusted.")

cable = RevealedMovable(6, False, buoy,
                        "CABLE",
                        "Caught around the BUOY is a CABLE.",
                        "A power cable, for transferring power from one place to another.")

jerry = RevealedMovable(6, False, buoy,
                        "JERRY",
                        "On the seabed lies a JERRY can.",
                        "Seems to be full of fuel.")

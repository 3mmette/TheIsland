from location import *
from item import *

loc_six = ExplorableLocation(6, 9, 12, 3, 5,
                             "there is a rocky shoreline.",
                             "the rocky shoreline.\nThe tide must be low as there are many things washed ashore.")

hex61 = Movable(6, True,
                "BLOCK SIX",
                "Among the things lies hexagonal BLOCK SIX.",
                "A hexagonal shaped rock, made of granite. The number six is engraved on it.",
                "On the ground lies the dropped hexagonal BLOCK SIX.")

# Fix these 3
jerry_can = "To create"
electrical_cable = "To create"
water_bottle = Movable(6, True,
                       "WATER BOTTLE",
                       "On the rocks lies a WATER BOTTLE.",
                       "A full bottle of natural spring water.",
                       "On the ground lies the dropped WATER BOTTLE.")

crackers = Consumable(6, True, 5, 0,
                      "CRACKERS",
                      "On the high tide mark sits a packet of CRACKERS.",
                      "A small packet of crackers, from the company Polly.",
                      "On the ground lies the dropped CRACKERS.",
                      "A little dry, but still tasty.")

beans = Consumable(6, True, 5, 1,
                   "BEANS",
                   "Jammed between two rocks is a can on BEANS.",
                   "This is a tasty treat.",
                   "On the ground lies the dropped BEANS.",
                   "They may make you gassy. but they are good.")

soup = Consumable(6, True, 8, 8,
                  "SOUP",
                  "A tin of SOUP lays discarded amongst the rocks.",
                  "Hydration and calories, what more do you want.",
                  "On the ground lies the dropped SOUP.",
                  "Meat, Veg and Soup. What a great meal.")

buoy = HasItem(6, True, ['a', 'b'], ['a', 'b'],
               "BUOY",
               "Floats in the water",
               "",
               "On the ground lies the dropped")

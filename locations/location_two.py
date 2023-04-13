from location import *
from item import *

loc_two = ExplorableLocation(2, 5, 3, 13, 1,
                             "there is a sandy beach with some palms.",
                             "the sandy beach.\nSmall waves crash onto the white sand.")

coconut_item = Item(2, False,
                    "HANGING COCONUT",
                    "On the PALM trees hang a few COCONUT.",
                    "Ripe and ready, they hang out of reach.")

coconut_consumable = Consumable(2, False, 5, 5,
                                "COCONUT",
                                "On the ground lays a COCONUT.",
                                "Ripe and ready to be consumed.",
                                "Delicious coconut water and flesh, yum yum.")

alcohol = Consumable(1, False, 0, -5,
                     "ALCOHOL",
                     "In the chest lies bottles of ALCOHOL",
                     "This stuff is pure, you could run a rocket of it.",
                     "It's way too string, making you throw up.")

hex21 = Movable(2, True,
                "BLOCK TWO",
                "Under the PALM trees lies hexagonal BLOCK TWO.",
                "A hexagonal shaped rock, made of granite. The number two is engraved on it.")

palm = RevealsMovable(2, True, coconut_item,
                      "PALM",
                      "A few PALM trees grow in the middle of the area.",
                      "Rising tall above you, a few COCONUT are out of reach.",
                      "The palms lay bare, just fronds up there")

wooden_chest = RevealsMovable(2, False, alcohol,
                              "WOODEN CHEST",
                              "An old WOODEN CHEST lies at the bottom of the hole.",
                              "Made of old wood, the chest is full with bottles of ALCOHOL.",
                              "The chest is empty.")

sand = ConditionalReveals(2, True, wooden_chest,
                          "SAND",
                          "Between the palms and the ocean there is a patch of SAND that is slightly different.",
                          "There seems to be razor sharp shells mixed into the sand.",
                          "A WOODEN CHEST lies at the bottom of the hole in the sand.")

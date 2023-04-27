from location import *
from item import *

loc_two = ExplorableLocation(2, "PALM", 5, 3, 13, 1,
                             "there is a sandy beach with some palms.",
                             "the sandy beach.\nSmall waves crash onto the white sand.")

palm = Reveals(2, True, None,
               "PALM",
               "A few PALM trees grow in the middle of the area.",
               "A desert island palm, it grows next to the ocean.\n"
               "It rises tall above you, a few COCONUT sit out of reach.")

coconut = ConditionalRevealedConsumable(2, False, 10, 10, palm,
                                        "COCONUT",
                                        "On the ground lays a COCONUT.",
                                        "Ripe and ready to be consumed.",
                                        "Delicious coconut water and flesh, yum yum.")
palm.set_revealed_item(coconut)

sand = ConditionalReveals(2, True, None,
                          "SAND",
                          "There is a patch of SAND that is slightly different.",
                          "There seems to be razor sharp shells mixed into the sand.",
                          "A WOODEN CHEST lies at the bottom of the hole in the sand.")

wooden_chest = RevealsMovable(2, False, None,
                              "WOODEN CHEST",
                              "An old WOODEN CHEST lies at the bottom of the hole.",
                              "Made of old wood, barnacles are encrusted on it.",
                              "The chest is full with bottles of ALCOHOL.",
                              "The chest is empty.")
sand._reveals_item = wooden_chest

alcohol = RevealedConsumable(2, False, 0, -5, wooden_chest,
                             "ALCOHOL",
                             "In the chest lies bottles of ALCOHOL",
                             "This stuff is pure, you could run a rocket of it.",
                             "It's way too string, making you throw up.")
wooden_chest.set_revealed_item(alcohol)

block_two = Movable(2, True,
                    "BLOCK 2",
                    "Under the PALM trees lies hexagonal BLOCK 2.",
                    "A hexagonal shaped rock, made of granite. The number two is engraved on it.")

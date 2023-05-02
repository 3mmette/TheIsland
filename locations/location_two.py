from classes.location import *
from classes.item import *

loc_two = ExplorableLocation(2, 711, "SANDY BEACH", 5, 3, 13, 1,
                             "there is a sandy beach with some palms.",
                             "the sandy beach.\nSmall waves crash onto the white sand.")

palm = RevealsMovable(2, True, None,
                      "PALM",
                      "A few PALM trees grow in the middle of the area.",
                      "A desert island palm, it grows next to the ocean.",
                      "It rises tall above you, a COCONUT sits out of reach.",
                      "It rises tall above you, but there are nothing but fronds")

coconut = Coconut(2, False, 10, 10, palm,
                  "COCONUT",
                  "In the palm sits a COCONUT.",
                  "Ripe and ready to be be broken open.",
                  "You could interact to knock it down, if you have the right item...",
                  "Laying in the sand under the palm is a COCONUT.",
                  "Delicious coconut water and flesh, yum yum.")
palm.set_revealed_item(coconut)

sand = ConditionalReveals(2, True, None,
                          "SAND",
                          "There is a patch of SAND that is slightly different.",
                          "There are razor sharp shells mixed into the sand, but something lies underneath\n"
                          "You could interact with it, if you have the right item...",
                          "A WOODEN CHEST lies at the bottom of the hole in the sand.")

wooden_chest = Container(2, False, None, None, False,
                         "WOODEN CHEST",
                         "An old WOODEN CHEST lies at the bottom of the hole in the sand.",
                         "Made of old wood, barnacles are encrusted on it.",
                         "The chest is full with bottles of ALCOHOL.",
                         "The chest is empty.")
sand._reveals_item = wooden_chest

alcohol = RevealedConsumable(2, False, 0, -5, wooden_chest,
                             "ALCOHOL",
                             "In the chest lies bottles of ALCOHOL",
                             "This stuff is pure, you could run a rocket of it.",
                             "It's way too string, making you throw up.")
wooden_chest.set_holds_item(alcohol)

block_two = Movable(2, True,
                    "BLOCK 2",
                    "Under the PALM trees lies hexagonal BLOCK 2.",
                    "A hexagonal shaped rock, made of granite. The number two is engraved on it.")

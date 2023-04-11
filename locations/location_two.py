from location import *
from item import *

loc_two = ExplorableLocation(2, 5, 3, 13, 1,
                             "there is a sandy beach with some palms.",
                             "the sandy beach.\nSmall waves crash onto the white sand.")

coconut = Consumable(2, False, 5, 5,
                     "COCONUT",
                     "On the PALM trees hang a few COCONUT.",
                     "A ripe coconut, ready to be consumed",
                     "On the ground lies the dropped COCONUT.",
                     "Delicious coconut water and flesh.")

alcohol = Consumable(2, False, 0, -5,
                     "ALCOHOL",
                     "In the chest lies bottles of ALCOHOL",
                     "This stuff is pure, you could run a rocket of it.",
                     "On the ground lies the dropped ALCOHOL",
                     "It's way too string, making you throw up.")

hex21 = Movable(2, True,
                "BLOCK TWO",
                "Under the PALM trees lies hexagonal BLOCK TWO.",
                "A hexagonal shaped rock, made of granite. The number two is engraved on it.",
                "On the ground lies the dropped hexagonal BLOCK TWO.")

palm = Holds(2, True, coconut, coconut,
             "PALM",
             "A few PALM trees grow in the middle of the area.",
             "Rising tall above you, a few COCONUT are out of reach.",
             "The palms lay bare, just fronds up there")

wooden_chest = Container(2, False, alcohol, alcohol,
                         "WOODEN CHEST",
                         "An old WOODEN CHEST lies at the bottom of the hole.",
                         "Made of old wood and encrusted with barnacles.",
                         "The chest is full with bottles of ALCOHOL.",
                         "The chest is empty.")

sand = Reveal(2, True, wooden_chest, False,
              "SAND",
              "Between the palms and the ocean there is a patch of SAND that is slightly different.",
              "There seems to be razor sharp shells mixed into the sand.",
              "A WOODEN CHEST lies at the bottom of the hole.")

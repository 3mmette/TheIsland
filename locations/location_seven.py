from location import *
from item import *

loc_seven = ExplorableLocation(7, 11, 8, 4, 12,
                               "there is a vegetated area with some medium sized trees.",
                               "the vegetated area.\nThe area seems to be man made with trees planted.")

hex71 = Movable(7, True,
                "BLOCK SEVEN",
                "Near a bush lies hexagonal BLOCK SEVEN.",
                "A hexagonal shaped rock, made of granite. The number seven is engraved on it.",
                "On the ground lies the dropped hexagonal BLOCK SEVEN.")

red_fruit = Consumable(7, False, -100, -100,
                       "RED FRUIT",
                       "On one of the trees is a single RED FRUIT",
                       "A round, smooth piece of fruit. The skin is red.",
                       "On the ground lies the dropped RED FRUIT",
                       "Poisonous from the first bite, bye bye.")

yellow_fruit = Consumable(7, False, 6, 0,
                          "YELLOW FRUIT",
                          "On one of the trees is a single YELLOW FRUIT",
                          "A round, smooth piece of fruit. The skin is yellow.",
                          "On the ground lies the dropped YELLOW FRUIT",
                          "Sweet and delicious.")

blue_fruit = Consumable(7, False, 6, 0,
                        "BLUE FRUIT",
                        "On one of the trees is a single BLUE FRUIT",
                        "A round, smooth piece of fruit. The skin is blue.",
                        "On the ground lies the dropped BLUE FRUIT",
                        "Sweet and delicious.")

green_fruit = Consumable(7, False, 8, 0,
                         "GREEN FRUIT",
                         "On one of the trees is a single GREEN FRUIT",
                         "A round, smooth piece of fruit. The skin is green.",
                         "On the ground lies the dropped GREEN FRUIT",
                         "The best piece of fruit you have ever eaten.")

orange_fruit = Consumable(7, False, -5, -5,
                          "ORANGE FRUIT",
                          "On one of the trees is a single ORANGE FRUIT",
                          "A round, smooth piece of fruit. The skin is orange.",
                          "On the ground lies the dropped ORANGE FRUIT",
                          "It makes you sick.")

purple_fruit = Consumable(7, False, -5, -5,
                          "PURPLE FRUIT",
                          "On one of the trees is a single PURPLE FRUIT",
                          "A round, smooth piece of fruit. The skin is purple.",
                          "On the ground lies the dropped PURPLE FRUIT",
                          "It makes you sick.")

fruit_trees = Reveal(7, True,
                     [red_fruit, yellow_fruit, blue_fruit, green_fruit, orange_fruit, purple_fruit],
                     True,
                     "FRUIT TREE",
                     "think of description",
                     "lots of fruit",
                     "the trees are empty")

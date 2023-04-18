from location import *
from item import *
from locations.location_four import spring

loc_seven = ExplorableLocation(7, "ORCHID", 11, 8, 4, 12,
                               "there is a vegetated area with some medium sized trees.",
                               "the vegetated area.\nThe area seems too neat to be natural.")

fruit_tree = FruitTree(7, True, [],
                       "FRUIT TREE",
                       "Most of the vegetation is FRUIT TREE.",
                       "It looks like someone has been cross breeding fruit trees.",
                       "There is a fruit of every kind.",
                       "there are still some fruit on the trees.",
                       "All the fruit has been taken.")

body = Reveals(7, True, None,
               "BODY",
               "There is a BODY lying on the ground.",
               "In one hand is a red piece of fruit.\n"
               "In the other is a NOTE.")

note = Note(7, False, spring,
            "NOTE",
            "In one hand of the body is a NOTE.",
            "It says 'You will find the key at the source'")
body._reveals = note

red_fruit = Consumable(7, False, -100, -100,
                       "RED FRUIT",
                       "On one of the trees is a single RED FRUIT",
                       "A round, smooth piece of fruit. The skin is red.",
                       "Poisonous from the first bite, bye bye.")
fruit_tree._reveals.append(red_fruit)

yellow_fruit = Consumable(7, False, 6, 0,
                          "YELLOW FRUIT",
                          "On one of the trees is a single YELLOW FRUIT",
                          "A round, smooth piece of fruit. The skin is yellow.",
                          "Sweet and delicious.")
fruit_tree._reveals.append(yellow_fruit)

blue_fruit = Consumable(7, False, 6, 0,
                        "BLUE FRUIT",
                        "On one of the trees is a single BLUE FRUIT",
                        "A round, smooth piece of fruit. The skin is blue.",
                        "Sweet and delicious.")
fruit_tree._reveals.append(blue_fruit)

green_fruit = Consumable(7, False, 8, 0,
                         "GREEN FRUIT",
                         "On one of the trees is a single GREEN FRUIT",
                         "A round, smooth piece of fruit. The skin is green.",
                         "The best piece of fruit you have ever eaten.")
fruit_tree._reveals.append(green_fruit)

orange_fruit = Consumable(7, False, -5, -5,
                          "ORANGE FRUIT",
                          "On one of the trees is a single ORANGE FRUIT",
                          "A round, smooth piece of fruit. The skin is orange.",
                          "It makes you sick.")
fruit_tree._reveals.append(orange_fruit)

purple_fruit = Consumable(7, False, -5, -5,
                          "PURPLE FRUIT",
                          "On one of the trees is a single PURPLE FRUIT",
                          "A round, smooth piece of fruit. The skin is purple.",
                          "It makes you sick.")
fruit_tree._reveals.append(purple_fruit)

block_seven = Movable(7, True,
                      "BLOCK 7",
                      "Near a bush lies hexagonal BLOCK 7.",
                      "A hexagonal shaped rock, made of granite. The number seven is engraved on it.")

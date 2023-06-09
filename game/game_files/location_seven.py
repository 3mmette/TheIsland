from game.classes.location import *
from game.classes.item import *
from game.game_files.location_four import original_spring
from random import randint
from random import sample

fruit_colours = ["RED FRUIT", "ORANGE FRUIT", "YELLOW FRUIT", "GREEN FRUIT", "BLUE FRUIT", "PURPLE FRUIT"]
death_index = randint(0, 5)
death = [None, -100, -100, "Poisonous from the first bite, death comes swiftly."]
bad_one = [None, -5, -5, "It makes you sick."]
bad_two = [None, -5, -5, "It makes you sick."]
good_one = [None, 6, 3, "Sweet and delicious."]
good_two = [None, 6, 3, "Sweet and delicious."]
best = [None, 10, 6, "The best piece of fruit you have ever eaten."]
if death_index == 0:
    death[0] = fruit_colours[0]
    bad_one[0] = fruit_colours[1]
    bad_two[0] = fruit_colours[5]
    good_one[0] = fruit_colours[2]
    good_two[0] = fruit_colours[4]
    best[0] = fruit_colours[3]
elif death_index == 1:
    death[0] = fruit_colours[1]
    bad_one[0] = fruit_colours[0]
    bad_two[0] = fruit_colours[2]
    good_one[0] = fruit_colours[5]
    good_two[0] = fruit_colours[3]
    best[0] = fruit_colours[4]
elif death_index == 2:
    death[0] = fruit_colours[2]
    bad_one[0] = fruit_colours[1]
    bad_two[0] = fruit_colours[3]
    good_one[0] = fruit_colours[0]
    good_two[0] = fruit_colours[4]
    best[0] = fruit_colours[5]
elif death_index == 3:
    death[0] = fruit_colours[3]
    bad_one[0] = fruit_colours[2]
    bad_two[0] = fruit_colours[4]
    good_one[0] = fruit_colours[1]
    good_two[0] = fruit_colours[5]
    best[0] = fruit_colours[0]
elif death_index == 4:
    death[0] = fruit_colours[4]
    bad_one[0] = fruit_colours[3]
    bad_two[0] = fruit_colours[5]
    good_one[0] = fruit_colours[2]
    good_two[0] = fruit_colours[0]
    best[0] = fruit_colours[1]
elif death_index == 5:
    death[0] = fruit_colours[5]
    bad_one[0] = fruit_colours[4]
    bad_two[0] = fruit_colours[0]
    good_one[0] = fruit_colours[3]
    good_two[0] = fruit_colours[1]
    best[0] = fruit_colours[2]

fruits = [death, bad_one, bad_two, good_one, good_two, best]

original_location_seven = ExplorableLocation(7, 528, "FRUIT ORCHID", 11, 8, 4, 12,
                                             "there is a vegetated area with some medium sized trees.",
                                             "the vegetated area.\nThe area seems too neat to be natural.")

original_fruit_tree = FruitTree(7, True, [],
                                "FRUIT TREE",
                                "Most of the vegetation is FRUIT TREE.",
                                "It looks like someone has been cross breeding fruit trees.\n"
                                "Related colours should indicate related effects.",
                                "There is a fruit for every color of the rainbow.",
                                "There are still some fruit on the trees.",
                                "All the fruit has been taken.")

original_body = Reveals(7, True, None,
                        "BODY",
                        "There is a BODY lying on the ground.",
                        "")

original_note = Note(7, False, None,
                     "NOTE",
                     "In one hand of the body is a NOTE.",
                     "It says 'You will find the key at the source, not at the mouth'")

original_red_fruit = RevealedConsumable(7, False, 0, 0, None,
                                        "RED FRUIT",
                                        "On one of the trees is a single RED FRUIT",
                                        "A round, smooth piece of fruit. The skin is red.",
                                        "")

original_orange_fruit = RevealedConsumable(7, False, 0, 0, None,
                                           "ORANGE FRUIT",
                                           "On one of the trees is a single ORANGE FRUIT",
                                           "A round, smooth piece of fruit. The skin is orange.",
                                           "")

original_yellow_fruit = RevealedConsumable(7, False, 0, 0, None,
                                           "YELLOW FRUIT",
                                           "On one of the trees is a single YELLOW FRUIT",
                                           "A round, smooth piece of fruit. The skin is yellow.",
                                           "")

original_green_fruit = RevealedConsumable(7, False, 0, 0, None,
                                          "GREEN FRUIT",
                                          "On one of the trees is a single GREEN FRUIT",
                                          "A round, smooth piece of fruit. The skin is green.",
                                          "")

original_blue_fruit = RevealedConsumable(7, False, 0, 0, None,
                                         "BLUE FRUIT",
                                         "On one of the trees is a single BLUE FRUIT",
                                         "A round, smooth piece of fruit. The skin is blue.",
                                         "")

original_purple_fruit = RevealedConsumable(7, False, 0, 0, None,
                                           "PURPLE FRUIT",
                                           "On one of the trees is a single PURPLE FRUIT",
                                           "A round, smooth piece of fruit. The skin is purple.",
                                           "")

original_block_seven = Movable(7, True,
                               "BLOCK 7",
                               "Near a bush lies hexagonal BLOCK 7.",
                               "A hexagonal shaped rock, made of granite. The number seven is engraved on it.")

for fruit in original_fruit_tree.get_revealed_item():
    for fruit_values in fruits:
        if fruit.get_name() == fruit_values[0]:
            fruit.set_energy_value(fruit_values[1])
            fruit.set_hydration_value(fruit_values[2])
            fruit.set_consumed_text(fruit_values[3])

original_fruit_tree.set_reveals_items_list(
    sample(original_fruit_tree.get_revealed_item(), len(original_fruit_tree.get_revealed_item())))

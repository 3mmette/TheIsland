from game.classes.location import *
from game.classes.item import *
from game.classes.backpack import BackPack
from game.classes.chart import Chart

backpack = BackPack()
chart = Chart()

location_zero = StartLocation(0, 834, "THE BOAT", 1, 13, 13, 13,
                              "there is a boat, tied to the small jetty.",
                              "the boat.\nIt slowly rocks back and forth in the ocean.",
                              "a boat.\nIt slowly rocks back and forth in the ocean.\n"
                              "It is tied to a small jetty and beyond lies The Island.")

dashboard = Dashboard(0, True, None,
                      "DASHBOARD",
                      "At the front of the boat there is a DASHBOARD.\n"
                      "It shows the status of a few things to get the boat started.",
                      "There is a BUTTON to start the boat",
                      "There is a slot to insert a key\n"
                      "You could interact to turn the chamber, if you have the right items...",
                      "You are able to turn the key slot, this step is complete.",
                      "The dashboard lies dormant, without any power running to it.",
                      "The dashboards lights are on, this step is complete.",
                      "The fuel gauge is sitting on empty.",
                      "The fuel gauge is on full, this step is complete.")

compartment = Compartment(0, True,
                          "COMPARTMENT",
                          "Under the dashboard is an open COMPARTMENT.",
                          "In the compartment there are two ways to power the boat.\n"
                          "You could interact to insert something, if you have the right items...",
                          "There are two battery leads, not connected to anything.",
                          "A marine battery in connected to the leads.",
                          "There is a socket a power cable could be plugged into.",
                          "There is a power cable plugged in.")

heavy_chest = Container(0, True, None, None, True,
                        "HEAVY CHEST",
                        "At the rear of the boat is a HEAVY CHEST.",
                        "The chest appears to be bolted to the floor.\n"
                        "There is a KEYPAD on the front.",
                        "A heavy marine BATTERY lies inside.",
                        "The chest is empty.")

fuel_tank = RequiresInsert(0, True,
                           "FUEL TANK",
                           "On the side there is a FUEL TANK.",
                           "Taking a look inside, you see it is empty.\n"
                           "You could interact to fill it, if you have the right items...",
                           "Taking a look inside, you see it is full.")

battery = RevealedMovable(0, False, heavy_chest,
                          "BATTERY",
                          "Inside the chest is a BATTERY",
                          "A large Battery with two terminals on top.")
heavy_chest.set_holds_item(battery)

button = FinalButton(0, False,
                     "BUTTON",
                     "On the dashboard there is a BUTTON.",
                     "The button could start the boat.\n"
                     "You could interact to start it, if the boat is ready...",
                     "Nothing happens.")
dashboard.set_revealed_item(button)

keypad = Keypad(0, False, "ISLE",
                "KEYPAD",
                "On the heavy chest is a KEYPAD.",
                "It seems to need a four letter password to unlock the chest.\n"
                "You could interact to enter the code, if you know it...")
heavy_chest.set_revealed_item(keypad)

block_zero = Movable(0, True,
                     "BLOCK 0",
                     "On the floor of the boat lies hexagonal BLOCK 0.",
                     "A hexagonal shaped rock, made of granite. The number zero is engraved on it.")

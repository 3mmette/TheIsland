from location import *
from item import *
from backpack import BackPack

backpack = BackPack(5)

location_zero = StartLocation(0, "BOAT", 1, 13, 13, 13,
                              "there is a boat, tied to the small jetty.",
                              "the boat.\nIt slowly rocks back and forth in the ocean.",
                              "a boat.\nIt slowly rocks back and forth in the ocean.\n"
                              "It is tied to a small jetty and beyond lies The Island.")

dashboard = Dashboard(0, True, None,
                      "DASHBOARD",
                      "At the front of the boat there is a DASHBOARD.",
                      "There is a BUTTON to start the boat",
                      "There is a slot to insert a key.",
                      "You are able to turn the key slot",
                      "The dashboard lies dormant, without any power running to it.",
                      "The dashboards lights are on.",
                      "The fuel gauge is sitting on empty.",
                      "The fuel gauge is on full")

compartment = Compartment(0, True,
                          "COMPARTMENT",
                          "Under the dashboard is an open COMPARTMENT.",
                          "Inside the compartment there are two ways to power the boat.",
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
                           "Taking a look inside, you see it is empty.",
                           "Taking a look inside, you see it is full.")

battery = Movable(0, False,
                  "BATTERY",
                  "Inside the chest is a BATTERY",
                  "A large Battery with two terminals on top.")
heavy_chest.set_holds_item(battery)

button = FinalButton(0, False,
                     "BUTTON",
                     "On the DASHBOARD there is a BUTTON.",
                     "The button could start the boat, if everything is working.",
                     "Nothing happens.")
dashboard.set_revealed_item(button)

keypad = Keypad(0, False, "ISLE",
                "KEYPAD",
                "On the heavy chest is a KEYPAD",
                "It seems to need a four letter password to unlock the chest.")
heavy_chest.set_revealed_item(keypad)

block_zero = Movable(0, True,
                     "BLOCK 0",
                     "On the floor of the boat lies hexagonal BLOCK 0.",
                     "A hexagonal shaped rock, made of granite. The number zero is engraved on it.")

from location import *
from item import *

location_zero = StartLocation(0, 1, 13, 13, 13,
                              "there is a boat, tied to the small jetty.",
                              "the boat.\nIt slowly rocks back and forth as it bobs on the ocean.",
                              "*** Create Start Text ***")

dashboard = Dashboard(0, True, None,
                      "DASHBOARD",
                      "At the front there is a DASHBOARD.",
                      "There is a BUTTON to start the boat",
                      "There is a slot to insert a key.",
                      "You are now able to turn the key slot",
                      "The dashboard lies dormant, without any power running to it.",
                      "The dashboards lights are on.",
                      "The fuel gauge is sitting on empty.",
                      "The fuel gauge is on full")

compartment = Compartment(0, True,
                          "COMPARTMENT",
                          "Under the DASHBOARD is a COMPARTMENT.",
                          "Inside the compartment it looks like the boat could be powered in two ways.",
                          "There are two battery leads, not connected to anything.",
                          "A marine battery in connected to the leads.",
                          "There is a socket a power cable could be plugged into.",
                          "There is a power cable plugged in, ready to jumpstart the boat.")

heavy_chest = HeavyChest(0, True, None, None,
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
                           "Taking a look inside, you see it is now full.")

battery = RevealedMovable(0, False, None,
                          "BATTERY",
                          "Inside the chest is a BATTERY",
                          "A large Battery with two terminals on top.")

button = FinalButton(0, False,
                     "BUTTON",
                     "On the DASHBOARD there is a BUTTON.",
                     "The button says PRESS BUTTON to start.",
                     "Nothing happens.",
                     "The boat starts.")
dashboard.reveals = button

keypad = Revealed(0, False, dashboard,
                  "KEYPAD",
                  "On the HEAVY CHEST is a KEYPAD",
                  "A typical keypad. It seems to need an input of four digits...")

hex01 = Movable(0, True,
                "BLOCK ZERO",
                "On the floor of the boat lies hexagonal BLOCK ZERO.",
                "A hexagonal shaped rock, made of granite. The number zero is engraved on it.")

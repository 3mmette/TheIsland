from location import *
from item import *

# Short descriptions follow a cardinal direction (To the North...).
# Long description follows a players choice of cardinal direction:
# For undiscovered locations (You arrive at...)
# For discovered locations (You return to...)

location_zero = StartLocation(0, 1, 13, 13, 13,
                              "there is a boat, tied to the small jetty.",
                              "the boat.\nIt slowly rocks back and forth as it bobs on the ocean.",
                              "*** Create Start Text ***")

battery = Movable(0, False,
                  "BATTERY",
                  "Inside the chest is a BATTERY",
                  "A large Battery with two terminals on top.")

hex01 = Movable(0, True,
                "BLOCK ZERO",
                "On the floor of the boat lies hexagonal BLOCK ZERO.",
                "A hexagonal shaped rock, made of granite. The number zero is engraved on it.")

button = Item(0, False,
              "BUTTON",
              "On the DASHBOARD there is a BUTTON.",
              "The button says PRESS to start.")

dashboard = Dashboard(0, True, button,
                      "DASHBOARD",
                      "At the front there is a DASHBOARD.",
                      "There is a BUTTON to start the boat",
                      "The dashboard lies dormant, without any power running to it.",
                      "The dashboards lights are on.",
                      "The fuel gauge is sitting on empty.",
                      "The fuel gauge is on full",
                      "There is a slot to insert a key.",
                      "You are able to turn the key slot")

compartment = Compartment(0, True, [battery, "POWER CABLE"],
                          "COMPARTMENT",
                          "Under the DASHBOARD is a COMPARTMENT.",
                          "A white compartment, with a handle to open.",
                          "Inside the compartment it looks like the boat could be powered in two ways.",
                          "There are two battery leads, not connected to anything.",
                          "A marine battery in connected to the leads.",
                          "There is a socket a power cable could be plugged into.",
                          "There is a power cable plugged in, ready to jumpstart the boat.")

keypad = Item(0, False,
              "KEYPAD",
              "On the HEAVY CHEST is a KEYPAD",
              "A typical keypad. It seems to need an input of four digits...")

heavy_chest = HeavyChest(0, True, keypad, battery,
                         "HEAVY CHEST",
                         "At the rear of the boat is a HEAVY CHEST.",
                         "The chest appears to be bolted to the floor.\n"
                         "There is a KEYPAD on the front.",
                         "A heavy marine BATTERY lies inside.",
                         "The chest is empty.")

fuel_tank = Requires(0, True, ["petrol", "alcohol"],
                     "FUEL TANK",
                     "On the side there is a FUEL TANK.",
                     "A silver cap could be opened to look inside.",
                     "Taking a look inside, you see it is empty.",
                     "Taking a look inside, you see it is now full.")

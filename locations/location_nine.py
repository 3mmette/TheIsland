from location import *
from item import *

loc_nine = ExplorableLocation(9, 11, 12, 6, 8,
                              "there is a shipwreck on the rocks.",
                              "the shipwreck.\nWaves crash violently onto the rocks.")

ship = RevealsMovable(9, True, None,
                      "SHIP",
                      "The bow of a SHIP is laying broken on the rocks.",
                      "Through a small hole, you can see a gold coin that is out of reach.",
                      "The bow sits empty, there is nothing inside.")

hex91 = Movable(9, True,
                "BLOCK NINE",
                "Near to hull the ship lies hexagonal BLOCK NINE.",
                "A hexagonal shaped rock, made of granite. The number nine is engraved on it.")

coin = RevealedMovable(9, False, ship,
                       "GOLD COIN",
                       "Laying in a little patch of sunlight in the bow glints a GOLD COIN",
                       "Made of solid gold, and a decent size.")
ship.reveals = coin

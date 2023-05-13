from game.classes.location import *
from game.classes.item import *

loc_nine = ExplorableLocation(9, 567, "SHIPWRECK", 11, 12, 6, 8,
                              "there is a shipwreck on the rocks.",
                              "the shipwreck.\nWaves crash violently onto the rocks.")

ship = DualRevealsMovable(9, True, [],
                          "SHIP",
                          "The bow of a SHIP is laying broken on the rocks.",
                          "Through a small hole you can see inside the hull.",
                          "A packet of CRACKERS lies just within reach.",
                          "There is nothing is close inside the hole.",
                          "A gold COIN can be seen further inside, but it's out of reach.",
                          "There is nothing deeper inside the hull.")

coin = ConditionalRevealedMovable(9, False, ship,
                                  "COIN",
                                  "Far inside the ship, in a little patch of sunlight glints a gold COIN.",
                                  "Made of solid gold, and a decent size.")
ship.set_revealed_item(coin)

crackers = RevealedConsumable(9, False, 10, 0, ship,
                              "CRACKERS",
                              "Just inside the hull sits a packet of CRACKERS.",
                              "A big packet of crackers, from the company Polly.",
                              "A little dry, but still tasty.")
ship.set_revealed_item(crackers)

block_nine = Movable(9, True,
                     "BLOCK 9",
                     "Near to hull the ship lies hexagonal BLOCK 9.",
                     "A hexagonal shaped rock, made of granite. The number nine is engraved on it.")

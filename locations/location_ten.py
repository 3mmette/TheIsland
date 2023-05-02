from classes.location import *
from classes.item import *

loc_ten = ExplorableLocation(10, 423, "GRANITE BLOCK", 11, 11, 8, 11,
                             "there is a small peninsula.",
                             "the peninsula.\nIt extends out a short distance into the ocean.")

block = Block(10, True,
              "BLOCK",
              "At the end of the peninsula is a rectangular BLOCK.",
              "Made of granite, there are three slots to insert items.\n"
              "You could interact with it, if you have the right items...")

shadow = Reveals(10, True, None,
                 "SHADOW",
                 "In the water below is a mysterious SHADOW.",
                 "The monster of the depths, a KRAKEN, swims below.")

kraken = Npc(10, False,
             "KRAKEN",
             "From just under the water, an eye of a KRAKEN watches you.",
             "It watches you intensely, almost lke it wants to tell you something",
             "In your head you hear a voice...\n"
             "Get the BLOCK right, and help you I might.\n"
             "Get it wrong, and in the depths you'll belong.")
shadow._reveals_item = kraken

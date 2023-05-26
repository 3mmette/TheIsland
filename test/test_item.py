import unittest
from game.classes.item import Item


class TestItem(unittest.TestCase):
    """
    A test suite for the Backpack class.
    """
    def setUp(self) -> None:
        """
        Prepare the test fixture.
        Reuses the "unit under test" across multiple tests, initialised it every time.
        """
        self.uut = Item(0, True, "ITEM", "Here is an ITEM.", "Look at me, I'm an item.")

    def test_unit_type(self):
        """
        Tests to see if the object is right type.
        """
        self.assertIsInstance(self.uut, Item)

    def test_item_discovery_status(self):
        """
        Tests getting the items discovery status.
        """
        self.assertFalse(self.uut.get_discovery_status())

    def test_an_item_being_discovered(self):
        """
        Tests an item being discovered.
        """
        self.uut.item_discovered()
        self.assertTrue(self.uut.get_discovery_status())


if __name__ == '__main__':
    unittest.main()

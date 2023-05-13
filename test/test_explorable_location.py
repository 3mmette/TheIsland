import unittest
from game.classes.location import ExplorableLocation
from game.classes.item import Item


class TestExplorableLocation(unittest.TestCase):
    """
    A test suite for the Backpack class.
    """
    def setUp(self) -> None:
        """
        Prepare the test fixture.
        Reuses the "unit under test" across multiple tests, initialised it every time.
        """
        self.uut = ExplorableLocation(0, 100, "Test Location", 1, 2, 3, 4, "A testing place", "Great place to test")

    def test_unit_type(self):
        """
        Tests to see if the object is right type.
        """
        self.assertIsInstance(self.uut, ExplorableLocation)

    def test_get_and_set_discovery_status(self):
        """
        Tests to see the original discovery status and once it has been discovered.
        """
        self.assertFalse(self.uut.get_discovery_status())

        self.uut.location_discovered()

        self.assertTrue(self.uut.get_discovery_status())

    def test_add_and_remove_item_to_location(self):
        new_item = Item(0, True, "Item", "I'm an item", "Long description of item")
        self.uut.add_item_to_location(new_item)

        self.assertEqual(self.uut.get_location_items(), [new_item])

        self.uut.remove_location_item(new_item)

        self.assertEqual(self.uut.get_location_items(), [])


if __name__ == '__main__':
    unittest.main()

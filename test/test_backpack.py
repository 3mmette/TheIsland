import unittest
from game.classes.backpack import BackPack
from game.classes.item import Movable


class TestBackpack(unittest.TestCase):
    """
    A test suite for the Backpack class.
    """
    def setUp(self) -> None:
        """
        Prepare the test fixture.
        Reuses the "unit under test" across multiple tests, initialised it every time.
        """
        self.uut = BackPack()

    def test_unit_type(self):
        """
        Tests to see if the object is right type.
        """
        self.assertIsInstance(self.uut, BackPack)

    def test_default_backpack_capacity(self):
        """
        Tests the default capacity of the backpack.
        """
        self.assertEqual(self.uut.get_capacity(), 5)

    def test_set_backpack_capacity(self):
        """
        Tests that the capacity of the backpack can be set to a different value.
        """
        self.uut.set_capacity(10)

        self.assertEqual(self.uut.get_capacity(), 10)

    def test_add_item(self):
        """
        Tests that a movable item can be added to the backpack.
        """
        new_item = Movable(0, True, "Item", "I'm an item", "Oooo shiny")
        self.uut.add(new_item)

        self.assertEqual(self.uut.items(), [new_item])

    def test_backpack_items_count(self):
        """
        Tests the number of items in the backpack can be found.
        """
        new_item_1 = Movable(0, True, "Item 1", "I'm the first item", "Oooo shiny")
        new_item_2 = Movable(0, True, "Item 2", "I'm the second item", "Oooo shiny")
        new_item_3 = Movable(0, True, "Item 3", "I'm the third item", "Oooo shiny")
        self.uut.add(new_item_1)
        self.uut.add(new_item_2)
        self.uut.add(new_item_3)

        self.assertEqual(self.uut.count(), 3)

    def test_backpack_items_sort(self):
        """
        Tests the items are sorted as they are added.
        """
        new_item_1 = Movable(0, True, "Bravo", "Bb", "Oooo shiny")
        new_item_2 = Movable(0, True, "Delta", "Dd", "Oooo shiny")
        new_item_3 = Movable(0, True, "Alpha", "Aa", "Oooo shiny")
        new_item_4 = Movable(0, True, "Charlie", "Cc", "Oooo shiny")
        self.uut.add(new_item_1)
        self.uut.add(new_item_2)
        self.uut.add(new_item_3)
        self.uut.add(new_item_4)

        self.assertEqual(self.uut.items(), [new_item_3, new_item_1, new_item_4, new_item_2])

    def test_backpack_item_limit(self):
        """
        Tests that it won't allow you to add more than the capacity.
        """
        new_item_1 = Movable(0, True, "Alpha", "Aa", "Oooo shiny")
        new_item_2 = Movable(0, True, "Bravo", "Bb", "Oooo shiny")
        new_item_3 = Movable(0, True, "Charlie", "Cc", "Oooo shiny")
        new_item_4 = Movable(0, True, "Delta", "Dd", "Oooo shiny")
        new_item_5 = Movable(0, True, "Echo", "Ee", "Oooo shiny")
        new_item_6 = Movable(0, True, "Foxtrot", "Ff", "Oooo shiny")
        self.uut.add(new_item_1)
        self.uut.add(new_item_2)
        self.uut.add(new_item_3)
        self.uut.add(new_item_4)
        self.uut.add(new_item_5)
        self.uut.add(new_item_6)

        self.assertEqual(self.uut.items(), [new_item_1, new_item_2, new_item_3, new_item_4, new_item_5])

    def test_in_backpack_binary_search(self):
        """
        Tests the function can get the index of an item in the backpack.
        """
        new_item_1 = Movable(0, True, "Alpha", "Aa", "Oooo shiny")
        new_item_2 = Movable(0, True, "Bravo", "Bb", "Oooo shiny")
        new_item_3 = Movable(0, True, "Charlie", "Cc", "Oooo shiny")
        new_item_4 = Movable(0, True, "Delta", "Dd", "Oooo shiny")
        new_item_5 = Movable(0, True, "Echo", "Ee", "Oooo shiny")
        self.uut.add(new_item_1)
        self.uut.add(new_item_2)
        self.uut.add(new_item_5)
        self.uut.add(new_item_3)
        self.uut.add(new_item_4)

        self.assertEqual(self.uut.in_backpack(new_item_5), 4)
        self.assertEqual(self.uut.in_backpack(new_item_3), 2)
        self.assertEqual(self.uut.in_backpack(new_item_1), 0)


if __name__ == '__main__':
    unittest.main()

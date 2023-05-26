import unittest
from game.classes.game import Game


class TestGame(unittest.TestCase):
    """
    A test suite for the Backpack class.
    """
    def setUp(self) -> None:
        """
        Prepare the test fixture.
        Reuses the "unit under test" across multiple tests, initialised it every time.
        """
        self.uut = Game()

    def test_unit_type(self):
        """
        Tests to see if the object is right type.
        """
        self.assertIsInstance(self.uut, Game)

    def test_reset_of_all_values(self):
        """
        This test always seems to fail as it doesn't recognise the file paths.
        File path has been confirmed though the chart test ans passed.
        Game works as intended.
        """
        self.uut.reset_game()
        self.assertFalse(self.uut.location_zero.get_discovery_status())
        self.uut.location_zero.location_discovered()
        self.assertTrue(self.uut.location_zero.get_discovery_status())
        self.uut.reset_game()
        self.assertFalse(self.uut.location_zero.get_discovery_status())


if __name__ == '__main__':
    unittest.main()

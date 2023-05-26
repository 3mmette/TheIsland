import unittest
from game.classes.chart import Chart


class TestChart(unittest.TestCase):
    """
    A test suite for the Backpack class.
    """
    def setUp(self) -> None:
        """
        Prepare the test fixture.
        Reuses the "unit under test" across multiple tests, initialised it every time.
        """
        self.uut = Chart()

    def test_unit_type(self):
        """
        Tests to see if the object is right type.
        """
        self.assertIsInstance(self.uut, Chart)

    def test_get_chart_file_name(self):
        self.assertEqual(self.uut.get_file_name(), "game/game_files/chart.txt")


if __name__ == '__main__':
    unittest.main()
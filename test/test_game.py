import unittest
from game.classes.game import Game


class TestGame:
    """
    A test suite for the Backpack class.
    """
    def setUp(self) -> None:
        """
        Prepare the test fixture.
        Reuses the "unit under test" across multiple tests, initialised it every time.
        """
        self.uut = Game()

    def test_reset(self):
        self.utt.alcohol.is_visable()
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()

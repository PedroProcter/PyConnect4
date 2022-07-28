import unittest
from pyconnect4.gameboard import GameBoard
from pyconnect4.game_referee import GameReferee

class TestGameReferee(unittest.TestCase):
    """Tests Game Referee"""

    def test_test_vertical_goal(self):
        """Test the test_vertical_goal method of GameReferee Class"""

        # Tests Positive Vertical Connect

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 1)
        testing_target_gameboard.place_token(0, 1)
        testing_target_gameboard.place_token(0, 1)
        output = testing_target_gameboard.place_token(0, 1)

        self.assertEqual(GameReferee.test_vertical_goal(testing_target_gameboard, output[1], 1), 1, "Player 1 should have win with vertical connect")

        testing_target_gameboard.place_token(1, 1)
        testing_target_gameboard.place_token(1, 1)
        testing_target_gameboard.place_token(1, 1)
        output = testing_target_gameboard.place_token(1, 1)

        self.assertEqual(GameReferee.test_vertical_goal(testing_target_gameboard, output[1], 1), 1, "Player 1 should have win with vertical connect")

        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 2)
        output = testing_target_gameboard.place_token(2, 2)

        self.assertEqual(GameReferee.test_vertical_goal(testing_target_gameboard, output[1], 2), 2, "Player 2 should have win with vertical connect")

        # Tests Negative Vertical Connect

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 1)
        testing_target_gameboard.place_token(0, 2)
        testing_target_gameboard.place_token(0, 1)
        output = testing_target_gameboard.place_token(0, 1)

        self.assertNotEqual(GameReferee.test_vertical_goal(testing_target_gameboard, output[1], 1), 1, "Player 1 shouldn't have win with vertical connect")

        testing_target_gameboard.place_token(1, 1)
        testing_target_gameboard.place_token(2, 1)
        testing_target_gameboard.place_token(1, 1)
        output = testing_target_gameboard.place_token(1, 1)

        self.assertNotEqual(GameReferee.test_vertical_goal(testing_target_gameboard, output[1], 1), 1, "Player 1 shouldn't have win with vertical connect")

    def test_test_horizontal_goal(self):
        """Test the test_horizontal_goal method of GameReferee Class"""

        # Tests Positive Horizontal Connect

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 1)
        testing_target_gameboard.place_token(1, 1)
        testing_target_gameboard.place_token(2, 1)
        output = testing_target_gameboard.place_token(3, 1)

        self.assertEqual(GameReferee.test_horizontal_goal(testing_target_gameboard, output[0], 1), 1, "Player 1 should have win with horizontal connect")

        testing_target_gameboard.place_token(0, 2)
        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(2, 2)
        output = testing_target_gameboard.place_token(3, 2)

        self.assertEqual(GameReferee.test_horizontal_goal(testing_target_gameboard, output[0], 2), 2, "Player 2 should have win with horizontal connect")
        
        # Tests Negative Horizontal Connect

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 1)
        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(2, 1)
        output = testing_target_gameboard.place_token(3, 1)

        self.assertNotEqual(GameReferee.test_horizontal_goal(testing_target_gameboard, output[0], 1), 1, "Player 1 shouldn't have win with horizontal connect")

        testing_target_gameboard.place_token(0, 2)
        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(4, 2)
        output = testing_target_gameboard.place_token(3, 2)

        self.assertNotEqual(GameReferee.test_horizontal_goal(testing_target_gameboard, output[0], 2), 2, "Player 2 shouldn't have win with horizontal connect")

    def test_test_right_diagonal_goal(self):
        """Test the test_horizontal_goal method of GameReferee Class"""

        # Tests Positive Horizontal Connect

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 1)

        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(1, 1)

        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 1)
        
        testing_target_gameboard.place_token(3, 2)
        testing_target_gameboard.place_token(3, 2)
        testing_target_gameboard.place_token(3, 2)
        output = testing_target_gameboard.place_token(3, 1)

        self.assertEqual(GameReferee.test_right_diagonal_goal(testing_target_gameboard, 1, output[1], output[0]), 1, "Player 1 should have win with right diagonal connect")

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 2)
        testing_target_gameboard.place_token(0, 2)
        testing_target_gameboard.place_token(0, 1)

        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(1, 1)

        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 1)
        
        testing_target_gameboard.place_token(3, 2)
        testing_target_gameboard.place_token(3, 2)
        testing_target_gameboard.place_token(3, 2)
        testing_target_gameboard.place_token(3, 2)
        testing_target_gameboard.place_token(3, 2)
        output = testing_target_gameboard.place_token(3, 1)

        self.assertEqual(GameReferee.test_right_diagonal_goal(testing_target_gameboard, 1, output[1], output[0]), 1, "Player 1 should have win with right diagonal connect")

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(4, 1)
        testing_target_gameboard.place_token(4, 1)
        testing_target_gameboard.place_token(4, 1)
        testing_target_gameboard.place_token(4, 2)

        testing_target_gameboard.place_token(3, 1)
        testing_target_gameboard.place_token(3, 1)
        testing_target_gameboard.place_token(3, 2)

        testing_target_gameboard.place_token(2, 1)
        testing_target_gameboard.place_token(2, 2)

        output = testing_target_gameboard.place_token(1, 2)

        self.assertEqual(GameReferee.test_right_diagonal_goal(testing_target_gameboard, 2, output[1], output[0]), 2, "Player 2 should have win with right diagonal connect")
        
        # Tests Negative Horizontal Connect

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 1)
        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(2, 1)
        output = testing_target_gameboard.place_token(3, 1)

        self.assertNotEqual(GameReferee.test_right_diagonal_goal(testing_target_gameboard, 1, output[1], output[0]), 1, "Player 1 shouldn't have win with right diagonal connect")

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 2)
        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(4, 2)
        output = testing_target_gameboard.place_token(3, 2)

        self.assertNotEqual(GameReferee.test_right_diagonal_goal(testing_target_gameboard, 2, output[1], output[0]), 2, "Player 1 shouldn't have win with right diagonal connect")

    def test_test_left_diagonal_goal(self):
        """Test the test_horizontal_goal method of GameReferee Class"""

        # Tests Positive Horizontal Connect

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(4, 1)

        testing_target_gameboard.place_token(3, 2)
        testing_target_gameboard.place_token(3, 1)

        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 1)
        
        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(1, 2)
        output = testing_target_gameboard.place_token(1, 1)

        self.assertEqual(GameReferee.test_left_diagonal_goal(testing_target_gameboard, 1, output[1], output[0]), 1, "Player 1 should have win with left diagonal connect")

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 1)
        testing_target_gameboard.place_token(0, 1)
        testing_target_gameboard.place_token(0, 1)
        testing_target_gameboard.place_token(0, 2)

        testing_target_gameboard.place_token(1, 1)
        testing_target_gameboard.place_token(1, 1)
        testing_target_gameboard.place_token(1, 2)

        testing_target_gameboard.place_token(2, 1)
        testing_target_gameboard.place_token(2, 2)

        output = testing_target_gameboard.place_token(3, 2)

        self.assertEqual(GameReferee.test_left_diagonal_goal(testing_target_gameboard, 2, output[1], output[0]), 2, "Player 2 should have win with left diagonal connect")
        
        # Tests Negative Horizontal Connect

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 1)
        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(2, 1)
        output = testing_target_gameboard.place_token(3, 1)

        self.assertNotEqual(GameReferee.test_left_diagonal_goal(testing_target_gameboard, 1, output[1], output[0]), 1, "Player 1 shouldn't have win with left diagonal connect")

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 2)
        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(4, 2)
        output = testing_target_gameboard.place_token(3, 2)

        self.assertNotEqual(GameReferee.test_left_diagonal_goal(testing_target_gameboard, 2, output[1], output[0]), 2, "Player 1 shouldn't have win with left diagonal connect")

    def test_test_goal(self):
        """Tests the test_goal method of GameReferee"""

        # left diagonal

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(4, 1)

        testing_target_gameboard.place_token(3, 2)
        testing_target_gameboard.place_token(3, 1)

        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 1)
        
        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(1, 2)
        output = testing_target_gameboard.place_token(1, 1)

        self.assertEqual(GameReferee.test_goal(testing_target_gameboard, 1, output[1], output[0]), 1, "Player 1 should have win with left diagonal connect")

        # right diagonal

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 1)

        testing_target_gameboard.place_token(1, 2)
        testing_target_gameboard.place_token(1, 1)

        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 2)
        testing_target_gameboard.place_token(2, 1)
        
        testing_target_gameboard.place_token(3, 2)
        testing_target_gameboard.place_token(3, 2)
        testing_target_gameboard.place_token(3, 2)
        output = testing_target_gameboard.place_token(3, 1)

        self.assertEqual(GameReferee.test_goal(testing_target_gameboard, 1, output[1], output[0]), 1, "Player 1 should have win with right diagonal connect")

        # horizontal

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 1)
        testing_target_gameboard.place_token(1, 1)
        testing_target_gameboard.place_token(2, 1)
        output = testing_target_gameboard.place_token(3, 1)

        self.assertEqual(GameReferee.test_goal(testing_target_gameboard, 1, output[1], output[0]), 1, "Player 1 should have win with horizontal connect")

        # vertical

        testing_target_gameboard = GameBoard(7, 6)

        testing_target_gameboard.place_token(0, 1)
        testing_target_gameboard.place_token(0, 1)
        testing_target_gameboard.place_token(0, 1)
        output = testing_target_gameboard.place_token(0, 1)

        self.assertEqual(GameReferee.test_goal(testing_target_gameboard, 1, output[1], output[0]), 1, "Player 1 should have win with vertical connect")
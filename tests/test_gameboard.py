import unittest
from pyconnect4.gameboard import GameBoard

class TestGameBoard(unittest.TestCase):

    def test_creation_gameboard(self):
        """Tests GameBoard Creation"""

        testing_target_gameboard = GameBoard(7, 6)

        #GameBoard Configuration Tests

        self.assertEqual(testing_target_gameboard.gameboard, [
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]
            ], "gameboard size should be 7x6")

    def test_token_placement(self):
        """Tests the place_token method of the class GameBoard"""
        testing_target_gameboard = GameBoard(7, 6)

        #GameBoard Changes Tests 

        testing_target_gameboard.place_token(0, 1)
        self.assertEqual(testing_target_gameboard.gameboard, [
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [1,0,0,0,0,0]
            ], "token position should be (0, 0)")
        
        testing_target_gameboard.place_token(0, 1)
        self.assertEqual(testing_target_gameboard.gameboard, [
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [1,0,0,0,0,0],
            [1,0,0,0,0,0]
            ], "token position should be (0, 0)")

        testing_target_gameboard.place_token(0, 2)
        self.assertEqual(testing_target_gameboard.gameboard, [
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [2,0,0,0,0,0],
            [1,0,0,0,0,0],
            [1,0,0,0,0,0]
            ], "token position should be (0, 0)")
        
        testing_target_gameboard.place_token(0, 1)
        self.assertNotEqual(testing_target_gameboard.gameboard, [
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [1,0,0,0,0,0]
            ], "token position should be (0, 0)")

        #Values returned Tests

        self.assertEqual(testing_target_gameboard.place_token(5, 2), [6, 5], "token position should be (6, 5)")

        self.assertEqual(testing_target_gameboard.place_token(5, 2), [5, 5], "token position should be (5, 5)")

        self.assertNotEqual(testing_target_gameboard.place_token(5, 2), [0, 5], "token position should be (4, 5)")
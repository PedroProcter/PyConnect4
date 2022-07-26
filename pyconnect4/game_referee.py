from .gameboard import GameBoard



class GameReferee:
    """GameReferee Docstring"""

    @staticmethod
    def test_horizontal_goal(gameboard: GameBoard, last_token_coordinate_y: int, player_token_id: int) -> int | bool:
        """Tests if the player have connected 4 token in horizontal"""
        goal_state = f"{player_token_id}{player_token_id}{player_token_id}{player_token_id}"

        horizontal_slots: list = [str(token) for token in gameboard.gameboard[last_token_coordinate_y]]

        if horizontal_slots.count(str(player_token_id)) >= 4:

            horizontal_slots = "".join(horizontal_slots)

            if goal_state in horizontal_slots:
                return player_token_id

        return False

    @staticmethod
    def test_vertical_goal(gameboard: GameBoard, last_token_coordinate_x: int, player_token_id: int) -> int | bool:
        """Tests if the player have connected 4 token in vertical"""
        goal_state = f"{player_token_id}{player_token_id}{player_token_id}{player_token_id}"

        vertical_slots: list = [str(token_row[last_token_coordinate_x]) for token_row in gameboard.gameboard]

        if vertical_slots.count(str(player_token_id)) >= 4:

            vertical_slots = "".join(vertical_slots)

            if goal_state in vertical_slots:
                return player_token_id

        return False

    @staticmethod
    def test_right_diagonal_goal(gameboard: GameBoard, player_token_id: int, last_token_coordinate_x: int, last_token_coordinate_y: int) -> int | bool:
        """Tests if the player have connected 4 token in (right) diagonal"""
        raise NotImplementedError

    @staticmethod
    def test_left_diagonal_goal(gameboard: GameBoard, player_token_id: int, last_token_coordinate_x: int, last_token_coordinate_y: int) -> int | bool:
        """Tests if the player have connected 4 token in (left) diagonal"""
        raise NotImplementedError

    @staticmethod
    def test_goal(gameboard: GameBoard, last_token_coordinates: tuple, player_token_id: int) -> int | bool:
        """Test if the player have reach the goal (win)"""

        if GameReferee.test_horizontal_goal(gameboard, last_token_coordinates, player_token_id) != False:
            return player_token_id

        if GameReferee.test_vertical_goal(gameboard, last_token_coordinates, player_token_id) != False:
            return player_token_id
        
        return False
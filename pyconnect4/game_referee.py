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
        tokens_collected = [str(player_token_id)]

        actual_token_index_x = last_token_coordinate_x
        actual_token_index_y = last_token_coordinate_y
        
        while actual_token_index_x < gameboard.columns - 1 and actual_token_index_y > 0:
            actual_token_index_y -= 1
            actual_token_index_x += 1

            tokens_collected.append(str(gameboard.gameboard[actual_token_index_y][actual_token_index_x]))

        actual_token_index_x = last_token_coordinate_x
        actual_token_index_y = last_token_coordinate_y

        while actual_token_index_x > 0 and actual_token_index_y < gameboard.rows - 1:
            actual_token_index_y += 1
            actual_token_index_x -= 1

            tokens_collected.insert(0, str(gameboard.gameboard[actual_token_index_y][actual_token_index_x]))

        if tokens_collected.count(str(player_token_id)):

            tokens_collected = "".join(tokens_collected)

            goal_state = f"{player_token_id}{player_token_id}{player_token_id}{player_token_id}"

            if goal_state in tokens_collected:
                return player_token_id

        return False     

    @staticmethod
    def test_left_diagonal_goal(gameboard: GameBoard, player_token_id: int, last_token_coordinate_x: int, last_token_coordinate_y: int) -> int | bool:
        """Tests if the player have connected 4 token in (left) diagonal"""
        tokens_collected = [str(player_token_id)]

        actual_token_index_x = last_token_coordinate_x
        actual_token_index_y = last_token_coordinate_y
        
        while actual_token_index_x > 0 and actual_token_index_y > 0:
            actual_token_index_y -= 1
            actual_token_index_x -= 1

            tokens_collected.append(str(gameboard.gameboard[actual_token_index_y][actual_token_index_x]))

        actual_token_index_x = last_token_coordinate_x
        actual_token_index_y = last_token_coordinate_y

        while actual_token_index_x < gameboard.columns - 1 and actual_token_index_y < gameboard.rows - 1:
            actual_token_index_y += 1
            actual_token_index_x += 1

            tokens_collected.insert(0, str(gameboard.gameboard[actual_token_index_y][actual_token_index_x]))

        if tokens_collected.count(str(player_token_id)):

            tokens_collected = "".join(tokens_collected)

            goal_state = f"{player_token_id}{player_token_id}{player_token_id}{player_token_id}"

            if goal_state in tokens_collected:
                return player_token_id

        return False     

    @staticmethod
    def test_goal(gameboard: GameBoard, player_token_id: int, last_token_coordinate_x: int, last_token_coordinate_y: int) -> int | bool:
        """Test if the player have reach the goal (win)"""

        if GameReferee.test_horizontal_goal(gameboard, last_token_coordinate_y, player_token_id) != False:
            return player_token_id

        elif GameReferee.test_vertical_goal(gameboard, last_token_coordinate_x, player_token_id) != False:
            return player_token_id

        elif GameReferee.test_right_diagonal_goal(gameboard, player_token_id, last_token_coordinate_x, last_token_coordinate_y) != False:
            return player_token_id

        elif GameReferee.test_left_diagonal_goal(gameboard, player_token_id, last_token_coordinate_x, last_token_coordinate_y) != False:
            return player_token_id
        
        return False
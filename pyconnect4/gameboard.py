



class GameBoard:
	"""GameBoard Docstring"""

	def __init__(self, board_vertical_size: int, board_horizontal_size: int) -> None:

		self.columns: int = board_horizontal_size
		self.rows: int = board_vertical_size

		self.gameboard = []
		
		for rows in range(board_vertical_size):
			row = []
			for columns in range(board_horizontal_size):
				row.append(0)

			self.gameboard.append(row)

	def place_token(self, column: int, player_token_id: int) -> list:
		"""Place a token in the lowest position of a column"""
		token_final_coordinates = [0, column]
		for index, row in enumerate(self.gameboard[::-1]):
			if row[column] == 0:
				row[column] = player_token_id
				token_final_coordinates[0] = abs(index - self.rows) -1
				break
		
		return token_final_coordinates

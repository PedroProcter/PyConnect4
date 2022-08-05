from .entities import User
from .gameboard import GameBoard
from .game_referee import GameReferee

from .ui.game_ui import GameUI

class Game:
    """Docstring for Game"""

    def __init__(self, game_ui: GameUI) -> None:
        self.game_ui = game_ui
        self.game_ui.initialize()

        self.gameboard = GameBoard(6, 7)

    def run(self) -> None:
        running = True

        self.game_ui.display_main_menu()

        self.gameboard.place_token(3, 1)
        self.gameboard.place_token(3, 2)
        
        while running:
            running = self.game_ui.events()
            self.game_ui.display_gameplay(self.gameboard)
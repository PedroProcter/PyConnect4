from pyconnect4.game import Game
from pyconnect4.ui.game_ui import GameGUI

def main():
    game_ui = GameGUI()
    game = Game(game_ui)
    game.run()

if __name__ == "__main__":
    main()
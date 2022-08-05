from abc import ABC, abstractclassmethod
from time import sleep

from pyconnect4.game_referee import GameReferee
from .gameboard_ui import GameBoardGUI
import os
import pygame



class GameUI(ABC):
    """GameUI Docstring"""

    def __init__(self):
        pass

    @abstractclassmethod
    def initialize(self):
        """Initialize User Interface"""
        pass

    @abstractclassmethod
    def events(self):
        """Events Handler"""
        pass

    @abstractclassmethod
    def display_main_menu(self):
        """Display Main Menu Screen"""
        pass

    @abstractclassmethod
    def display_gameplay(self):
        """Display GamePlay Screen"""
        pass
    
class GameGUI(GameUI):
    """GameGUI Docstring"""

    def __init__(self):
        pygame.display.init()
        pygame.font.init()

        self.SCREEN_SIZE = (790, 680)

        self.CLOCK = pygame.time.Clock()
        self.FPS_LOCK = 60

        self.SCREENRECT = pygame.Rect(0, 0, self.SCREEN_SIZE[0], self.SCREEN_SIZE[1])
        self.WINDOW_TITLE = "PyConnect4"

        self.DEFAULT_FONT = os.path.abspath("pyconnect4/ui/assets/fonts/yoster.ttf")

        self.BACKGROUND_COLOR = pygame.Color(48, 48, 48)
        self.TEXT_COLOR = pygame.Color(255, 255, 255)

        self.gameboard_ui = GameBoardGUI()

    def initialize(self):
        self.CLOCK.tick(self.FPS_LOCK)

        pygame.display.set_caption(self.WINDOW_TITLE)
        
        self.SCREEN = pygame.display.set_mode(self.SCREENRECT.size)
        
    def events(self):
        running = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()

                running = False
                return running

        return running

    def display_main_menu(self):

        self.SCREEN.fill(self.BACKGROUND_COLOR)
        while True:

            MENU_TEXT = pygame.font.Font(self.DEFAULT_FONT, 86).render("Menu", True, self.TEXT_COLOR)
            ALIGN_MENU_CENTER_X = (self.SCREEN_SIZE[0] / 2) - (MENU_TEXT.get_size()[0] / 2)
            self.SCREEN.blit(MENU_TEXT, (ALIGN_MENU_CENTER_X, 100))

            PLAY_BUTTON_TEXT = pygame.font.Font(self.DEFAULT_FONT, 16).render("~ Press ENTER to Play ~", True, self.TEXT_COLOR)
            ALIGN_PLAY_BUTTON_CENTER_X = (self.SCREEN_SIZE[0] / 2) - (PLAY_BUTTON_TEXT.get_size()[0] / 2)
            self.SCREEN.blit(PLAY_BUTTON_TEXT, (ALIGN_PLAY_BUTTON_CENTER_X, 300))

            pygame.display.update()
            
            self.events()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                break

    def display_gameplay(self, gameboard):
        """Display GamePlay Screen"""
        self.SCREEN.fill(self.BACKGROUND_COLOR)
        self.gameboard_ui.display_gameboard(gameboard, self.SCREEN)
        token_coordinates = gameboard.place_token(self.gameboard_ui.display_place_token(self.SCREEN),1)
        self.gameboard_ui.display_gameboard(gameboard, self.SCREEN)
        pygame.display.update()
        if GameReferee.test_goal(gameboard, 1, token_coordinates[1], token_coordinates[0]) != 0:
            print("player {1} wins")
        sleep(2)
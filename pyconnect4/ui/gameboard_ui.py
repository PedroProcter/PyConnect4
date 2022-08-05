from abc import ABC, abstractclassmethod
import os
import pygame

class GameBoardUI(ABC):
    """"""

    @abstractclassmethod
    def display_gameboard(self):
        """"""
        pass

    @abstractclassmethod
    def display_tokens(self, color):
        """"""
        pass

class GameBoardGUI(GameBoardUI):
    """"""

    def display_gameboard(self, gameboard, screen):
        """"""
        SCREEN_SIZE = (screen.get_size()[0], screen.get_size()[1])
        SLOTS_SIZE = (80, 80)
        SLOTS_SPACER_PIXELS = 16 + 80

        CURRENT_SLOT_COORDINATES = [SLOTS_SPACER_PIXELS, SLOTS_SPACER_PIXELS]

        SLOTS_COLOR = (55,55,55)

        SLOT_BORDER_RADIUS = 7

        self.GAMEBOARD_SURFACE = pygame.Surface(SCREEN_SIZE)
        self.GAMEBOARD_SURFACE.fill(pygame.Color(48, 48, 48))

        for row in range(6):
            for column in range(7):
                SLOT = pygame.Rect(CURRENT_SLOT_COORDINATES[0], CURRENT_SLOT_COORDINATES[1], SLOTS_SIZE[0], SLOTS_SIZE[1])
                pygame.draw.rect(self.GAMEBOARD_SURFACE, SLOTS_COLOR, SLOT, border_radius = SLOT_BORDER_RADIUS)

                CURRENT_SLOT_COORDINATES[0] += SLOTS_SPACER_PIXELS

            CURRENT_SLOT_COORDINATES[1] += SLOTS_SPACER_PIXELS

            CURRENT_SLOT_COORDINATES[0] = SLOTS_SPACER_PIXELS

        screen.blit(self.GAMEBOARD_SURFACE, (-30,0))

        self.display_tokens(gameboard.gameboard, screen)
        

    def display_tokens(self, gameboard, screen):
        """"""

        FIRST_TOKEN_COLOR = (110,55,55)
        SECOND_TOKEN_COLOR = (55,55,110)
        TOKEN_BORDER_RADIUS = 100
        TOKEN_SIZE = (60, 60)
        TOKEN_SPACER = 35 + 60
        
        CURRENT_TOKEN_COORDINATES = [TOKEN_SPACER, TOKEN_SPACER]

        GAMEBOARD = gameboard
        #print(GAMEBOARD)
        for row in GAMEBOARD:
            
            for column in row:
                

                if column == 0:
                    pass

                elif column == 1:
                    TOKEN = pygame.Rect(CURRENT_TOKEN_COORDINATES[0], CURRENT_TOKEN_COORDINATES[1], TOKEN_SIZE[0], TOKEN_SIZE[1])
                    pygame.draw.rect(screen, FIRST_TOKEN_COLOR, TOKEN, border_radius = TOKEN_BORDER_RADIUS)

                elif column == 2:
                    TOKEN = pygame.Rect(CURRENT_TOKEN_COORDINATES[0], CURRENT_TOKEN_COORDINATES[1], TOKEN_SIZE[0], TOKEN_SIZE[1])
                    pygame.draw.rect(screen, SECOND_TOKEN_COLOR, TOKEN, border_radius = TOKEN_BORDER_RADIUS)

                CURRENT_TOKEN_COORDINATES[0] += TOKEN_SPACER

            CURRENT_TOKEN_COORDINATES[0] = TOKEN_SPACER
            CURRENT_TOKEN_COORDINATES[1] += TOKEN_SPACER
                    
    def display_place_token(self, screen):
        """"""
        DEFAULT_FONT = os.path.abspath("pyconnect4/ui/assets/fonts/yoster.ttf")
        TEXT_COLOR = pygame.Color(255, 255, 255)
        SCREEN_SIZE = screen.get_size()

        while True:
            MENU_TEXT = pygame.font.Font(DEFAULT_FONT, 24).render("Press 1 to 7 to choose a column", True, TEXT_COLOR)
            ALIGN_MENU_CENTER_X = (SCREEN_SIZE[0] / 2) - (MENU_TEXT.get_size()[0] / 2)
            screen.blit(MENU_TEXT, (ALIGN_MENU_CENTER_X, 25))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_0]:
                return 0
            elif keys[pygame.K_1]:
                return 1
            elif keys[pygame.K_2]:
                return 2
            elif keys[pygame.K_3]:
                return 3
            elif keys[pygame.K_4]:
                return 4
            elif keys[pygame.K_5]:
                return 5
            elif keys[pygame.K_6]:
                return 6

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    exit()

            pygame.display.update()
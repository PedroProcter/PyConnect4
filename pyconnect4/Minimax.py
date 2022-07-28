from tkinter.tix import MAX
from .gameboard import GameBoard
from .game_referee import GameReferee

class Minimax:

    def Mini(gameboard: GameBoard,last_token_coordinates: tuple, player_token_id: int):
        global played_machine
        ##refisar
        if GameReferee.test_goal(gameboard,last_token_coordinates,player_token_id):
            return(player_token_id(gameboard.gameboard)0)
        #POSIBLES JUGADAS 
        movement = []
        last_token_coordinates=gameboard.gameboard
        for move in range (0,len(last_token_coordinates)):
            if gameboard[move]==0:
                gameboardaux = gameboard[:]
                gameboardaux[move] = move
                punctuation= Minimax(gameboardaux,move*(-1))
                movement.append([punctuation,move]) 
        
        if player_token_id == MAX:
            movement = max(movement)
            played_machine= movement[1]
            return movement
        else:
            movement=min(movement)
            return movement[0]



from abc import ABC, abstractmethod
from dataclasses import dataclass
from .game_referee import GameReferee

from pyparsing import oneOf

from .gameboard import GameBoard


@dataclass(init=True, repr=True, frozen=True)
class Player(ABC):
    ID: int
    Name: str

    @abstractmethod
    def get_next_move(self) -> int:
        pass

class User(Player):

    def get_next_move(self) -> int:
        raise NotImplementedError

class Machine(Player):

    def get_next_move(self, gameboard: GameBoard) -> int:
        raise NotImplementedError

    def compute_minimax(gameboard: GameBoard,last_token_coordinates: tuple, player_token_id: int): #quite el int 
        global played_machine
        ##refisar
        if GameReferee.test_goal(gameboard,last_token_coordinates,player_token_id):
            return(gameboard.gameboard,0)
        #POSIBLES JUGADAS 
        movement = []
        last_token_coordinates=gameboard.gameboard


        while last_token_coordinates.columns[x] !=6 and last_token_coordinates.row[y] != 7:
            x+=1
            last_token_coordinates   =  last_token_coordinates.columns[x],last_token_coordinates.row[y]

            if  last_token_coordinates.columns[x] !=6:
                y+=1
                last_token_coordinates.row[y]

        for move in range (0,len(last_token_coordinates)):
            if gameboard[move]==0:
                gameboardaux = gameboard
                gameboardaux.place_token[move] = player_token_id
                punctuation= Machine.compute_minimax(gameboardaux,move,player_token_id)#el menos unos estas porque no se cual es el aide del pc
                movement.append([punctuation,move]) 
        
        if player_token_id == MAX:
            movement = max(movement)
            played_machine= movement[1] 
            return movement
        else:
            movement=min(movement)
            return movement[0]












        raise NotImplementedError
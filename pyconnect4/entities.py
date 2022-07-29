from abc import ABC, abstractmethod
from asyncio.windows_events import NULL
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
        if User.get_next_move()==played_machine: 
            last_token_coordinates   =  gameboard.columns,gameboard.rows
            compro=GameReferee.test_goal(gameboard,last_token_coordinates,self.ID)
            if GameReferee.test_goal(gameboard,last_token_coordinates,self.ID)==False:
                movement = Machine.compute_minimax(gameboard,self.ID)
                gameboard[played_machine]=self.ID
                return gameboard
            return compro 

        raise NotImplementedError

    def compute_minimax(gameboard: GameBoard,last_token_coordinates:tuple, player_token_id: int): #quite el int 
        global played_machine
        ##refisar
        if GameReferee.test_goal(gameboard,last_token_coordinates,player_token_id):
            return(gameboard,0)
        #POSIBLES JUGADAS 
        movement = []
 

        while gameboard.columns[x] !=6 and gameboard.rows[y] != 7:
            x+=1
            last_token_coordinates   =  gameboard.columns[x],gameboard.rows[y]

            if  gameboard.columns[x] !=6:
                y+=1
                gameboard.rows[y]

        for move in range (0,len(last_token_coordinates)):
            if gameboard[move]==NULL:
                gameboardaux = gameboard
                gameboardaux.place_token[move] = player_token_id
                punctuation= Machine.compute_minimax(gameboardaux,last_token_coordinates,player_token_id)#el menos unos estas porque no se cual es el aide del pc
                movement.append([punctuation,move]) 
        
        #quite la condicional porque no tenia logica alguna
        movement = max(movement)
        played_machine= movement[1] 
        return movement
        
        
        
            












        raise NotImplementedError
from abc import ABC, abstractmethod
from dataclasses import dataclass


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
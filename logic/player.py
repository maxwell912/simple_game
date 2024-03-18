from enum import Enum


class PlayerName(Enum):
    RED = 'red'
    BLUE = 'blue'
    GRAY = 'gray'


class Player:
    START_GOLD = 1000

    def __init__(self, id: PlayerName):
        self.id = id.value
        self.gold = Player.START_GOLD

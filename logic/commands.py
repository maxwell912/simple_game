from logic.directions import Direction
from logic.game_map import GameMap
from logic.game_objects.army import Army
from logic.game_objects.castle import Castle
from logic.game_objects.game_object import WithIncome


class Command:
    pass

class NoneCommand(Command):
    pass

class MoveArmy(Command):
    def __init__(self, army: Army, direction: Direction):
        self.army = army
        self.direction = direction

class SpawnArmy(Command):
    def __init__(self, castle: Castle, size: int):
        self.castle = castle
        self.size = size

class MakeIncome(Command):
    def __init__(self, game_map: GameMap):
        for l in game_map.field_map:
            for obj in l:
                if isinstance(obj, WithIncome):
                    obj.get_income()
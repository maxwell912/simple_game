from __future__ import annotations

from logic.directions import Direction
from logic.game_map import GameMap
from logic.game_objects.army import Army
from logic.game_objects.castle import Castle
from logic.game_state import Command, NoneCommand, MoveArmy, SpawnArmy
from logic.player import Player


class Strategist:
    def __init__(self, player: Player):
        self.player = player
    
    def make_command(self, obj: Army | Castle, game_map: GameMap) -> Command:
        return NoneCommand


class MyStrategist(Strategist):
    def __init__(self, player: Player):
        super().__init__(player)
    
    def make_command(self, obj: Army | Castle, game_map: GameMap) -> Command:
        if isinstance(obj, Army):
            return MoveArmy(obj, Direction.RIGHT)
        elif isinstance(obj, Castle):
            return SpawnArmy(obj, int(obj.player.gold / obj.unit_cost))
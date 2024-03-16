from logic.game_map import GameMap
from logic.game_objects.army import Army
from logic.player import Player


class GameObject:
    def __init__(self, x: int, y: int, game_map: GameMap):
        self.x = x
        self.y = y
        self.game_map = game_map

    def get_image_path(self) -> str:
        return ''


class Location(GameObject):
    def __init__(self, x: int, y: int, game_map: GameMap):
        super().__init__(x, y, game_map)

    def handle_army(self, army: Army):
        if isinstance(self, HasPlayer):
            self.set_player(army.player)


class HasPlayer:
    def __init__(self, player: Player):
        self.player = player

    def set_player(self, new_player: Player):
        self.player = new_player


class MovableGameObject(GameObject):
    def __init__(self, x: int, y: int, game_map: GameMap):
        super().__init__(x, y, game_map)

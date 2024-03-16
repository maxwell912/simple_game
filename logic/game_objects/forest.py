from logic.game_map import GameMap
from logic.game_objects.game_object import GameObject


class Forest(GameObject):

    def __init__(self, x: int, y: int, game_map: GameMap):
        super().__init__(x, y, game_map)

    def get_image_path(self) -> str:
        return 'forest.png'

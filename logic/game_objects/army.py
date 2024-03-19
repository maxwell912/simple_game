from logic.game_objects.game_object import HasPlayer, GameObject
from logic.player import Player


class Army(GameObject, HasPlayer):
    def __init__(self, player: Player, size: int):
        HasPlayer.__init__(self, player)
        self.size = size

    def add(self, recruits: int):
        self.size += recruits

    def remove(self, casualties: int):
        self.size -= casualties

    def get_image_path(self) -> str:
        return 'army-' + str(self.player.id) + '.png'

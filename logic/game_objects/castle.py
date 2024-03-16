from logic.game_map import GameMap
from logic.game_objects.army import Army
from logic.game_objects.game_object import Location, HasPlayer
from logic.player import Player


class Castle(Location, HasPlayer):
    UNIT_COST = 100
    class_code = 'C'

    def __init__(self, player: Player, x: int, y: int, game_map: GameMap):
        Location.__init__(self, x, y, game_map)
        HasPlayer.__init__(self, player)

    def spawn_army(self, size: int):
        if self.player.gold >= Castle.UNIT_COST * size:
            self.player.gold -= Castle.UNIT_COST * size
            army = Army(self.player, size, self.x, self.y, self.game_map)
            self.game_map.set_object(self.x, self.y, army)

    def handle_army(self, army: Army):
        self.player = army.player


    def get_image_path(self) -> str:
        return 'castle-' + str(self.player.id) + '.png'

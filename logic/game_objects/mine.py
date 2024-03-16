from logic.game_objects.game_object import Location, HasPlayer
from logic.player import Player


class Mine(Location, HasPlayer):

    def __init__(self, income: int, player: Player, x: int, y: int):
        Location.__init__(self, x, y)
        HasPlayer.__init__(self, player)
        self.income = income

    def sell_ore(self):
        self.player.gold += self.income

    def get_image_path(self) -> str:
        return 'mine.png'

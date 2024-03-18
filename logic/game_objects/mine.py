from logic.game_objects.game_object import Location, HasPlayer, WithIncome
from logic.player import Player


class Mine(Location, WithIncome):

    def __init__(self, income: int, player: Player):
        WithIncome.__init__(self, income, player)

    def sell_ore(self):
        self.player.gold += self.income

    def get_image_path(self) -> str:
        return 'mine-' + str(self.player.id) + '.png'

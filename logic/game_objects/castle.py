from logic.game_objects.game_object import Location, WithIncome
from logic.player import Player


class Castle(Location, WithIncome):

    def __init__(self, player: Player, unit_cost: int, income: int):
        WithIncome.__init__(self, income, player)
        self.unit_cost = unit_cost

    def handle_player(self, player: Player):
        self.player = player

    def get_image_path(self) -> str:
        return 'castle-' + str(self.player.id) + '.png'

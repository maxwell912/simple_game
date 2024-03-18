from logic.game_map import GameMap
from logic.game_objects.castle import Castle
from logic.game_objects.forest import forest
from logic.game_objects.mine import Mine
from logic.game_objects.road import *
from logic.player import Player

def reverse(field):
    r = []
    for x in range(len(field[0])):
        c = []
        r.append(c)
        for y in range(len(field)):
            c.append(field[y][x])
    return r

class SimpleMap:
    def create(player1: Player, player2: Player):
        m = GameMap(10, 5)

        mine1 = lambda: Mine(10, player1)
        mine2 = lambda: Mine(10, player2)

        castle1 = lambda: Castle(player1, 10, 50)
        castle2 = lambda: Castle(player2, 10, 50)

        field = [
            [mine1(), forest, forest, forest, forest, forest, forest, forest, forest, mine2()],
            [Road02, forest, forest, forest, forest, forest, forest, forest, forest, Road02],
            [castle1(), Road13, Road13, Road13, Road13, Road13, Road13, Road13, Road13, castle2()],
            [Road02, forest, forest, forest, forest, forest, forest, forest, forest, Road02],
            [mine1(), forest, forest, forest, forest, forest, forest, forest, forest, mine2()],
        ]

        m.field_map = reverse(field)

        return m

from __future__ import annotations

from logic.directions import Direction
from logic.game_objects.army import Army
from logic.game_objects.castle import Castle
from logic.game_objects.forest import forest
from logic.game_objects.game_object import GameObject, Location
from logic.player import Player


class GameMap:
    def __init__(self, size_x: int, size_y: int):
        self.size_x = size_x
        self.size_y = size_y
        self.field_map = [[forest for _ in range(size_y)] for _ in range(size_x)]
        self.army_map = [[None for _ in range(size_y)] for _ in range(size_x)]

    def get_location(self, x: int, y: int) -> Location:
        return self.field_map[x][y]

    def get_object(self, x: int, y: int) -> GameObject | None:
        return self.army_map[x][y]

    def get_armies(self, player: Player) -> list[Army]:
        a = []
        for c in self.army_map:
            for obj in c:
                if isinstance(obj, Army) and obj.player is player:
                    a.append(obj)
        return a

    def get_castles(self, player: Player) -> list[Castle]:
        a = []
        for c in self.field_map:
            for obj in c:
                if isinstance(obj, Castle) and obj.player is player:
                    a.append(obj)
        return a

    def spawn_army(self, castle: Castle, size: int):
        player = castle.player
        if size > 0 and player.gold >= castle.unit_cost * size:
            player.gold -= castle.unit_cost * size
            x, y = self.get_coords(castle)
            army = Army(player, size, x, y)
            self.set_object(x, y, army)

    def move_army(self, army: Army, direction: Direction):
        x, y = self.get_coords(army)
        new_x, new_y = x + direction.value[0], y + direction.value[1]
        if new_x >= self.size_x or new_y >= self.size_y:
            return
        field = self.field_map[new_x][new_y]
        if isinstance(field, Location):
            target_obj = self.army_map[new_x][new_y]
            if target_obj is None:
                self.move(army, new_x, new_y)
                field.handle_player(army.player)
            elif isinstance(target_obj, Army):
                if army.player is target_obj.player:
                    target_obj.add(army.size)
                    self.clear(x, y)
                else:
                    enemy_army = target_obj
                    if army.size > enemy_army.size:
                        army.remove(enemy_army.size)
                        self.move(army, new_x, new_y)
                        field.handle_player(army.player)
                    elif army.size < enemy_army.size:
                        enemy_army.remove(army.size)
                        self.clear(x, y)
                    else:
                        self.army_map[new_x][new_y] = None
                        self.clear(x, y)
            else:
                raise RuntimeError('На карте объектов что то кроме армии')

    def set_object(self, x: int, y: int, obj: GameObject):
        if isinstance(obj, Army):
            old_value = self.get_object(x, y)
            if isinstance(old_value, Army):
                old_value.size += obj.size
            else:
                self.army_map[x][y] = obj
        else:
            raise RuntimeError('Заспавнилось что то кроме армии')

    def move(self, obj: GameObject, new_x: int, new_y: int):
        self.army_map[obj.x][obj.y] = None
        self.army_map[new_x][new_y] = obj
        obj.x = new_x
        obj.y = new_y

    def clear(self, x: int, y: int):
        self.army_map[x][y] = None

    def get_coords(self, obj):
        l = []
        if isinstance(obj, Army):
            l = self.army_map
        else:
            l = self.field_map

        for x in range(self.size_x):
            for y in range(self.size_y):
                if l[x][y] is obj:
                    return x, y
        raise RuntimeError('Координаты объекта не найдены')

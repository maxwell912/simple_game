from __future__ import annotations

from logic.directions import Direction
from logic.game_objects.army import Army
from logic.game_objects.game_object import GameObject, Location


class GameMap:
    def __init__(self, size_x: int, size_y: int):
        self.size_x = size_x
        self.size_y = size_y
        self.field_map = [[None for _ in range(size_x)] for _ in range(size_y)]
        self.object_map = [[None for _ in range(size_x)] for _ in range(size_y)]

    def get_location(self, x: int, y: int) -> Location:
        return self.field_map[x][y]

    def get_object(self, x: int, y: int) -> GameObject | None:
        return self.object_map[x][y]

    def move_army(self, army: Army, direction: Direction):
        new_x, new_y = army.x + direction.value[0], army.y + direction.value[1]
        field = self.field_map[new_x][new_y]
        if isinstance(field, Location):
            target_obj = self.object_map[new_x][new_y]
            if target_obj is None:
                self.move(army, new_x, new_y)
                field.handle_army(army)
            elif isinstance(target_obj, Army):
                if army.player is target_obj.player:
                    target_obj.add(army.size)
                    self.clear(army.x, army.y)
                else:
                    enemy_army = target_obj
                    if army.size > enemy_army.size:
                        army.remove(enemy_army.size)
                        self.move(army, new_x, new_y)
                        field.handle_army(army)
                    elif army.size < enemy_army.size:
                        enemy_army.remove(army.size)
                        self.clear(army.x, army.y)
                    else:
                        self.object_map[new_x][new_y] = None
                        self.clear(army.x, army.y)
            else:
                raise RuntimeError('На карте объектов что то кроме армии')

    def set_object(self, x: int, y: int, obj: GameObject):
        if isinstance(obj, Army):
            old_value = self.get_object(x, y)
            if isinstance(old_value, Army):
                old_value.size += obj.size
            else:
                self.object_map[x][y] = obj
        else:
            raise RuntimeError('Заспавнилось что то кроме армии')

    def move(self, obj: GameObject, new_x: int, new_y: int):
        self.object_map[obj.x][obj.y] = None
        self.object_map[new_x][new_y] = obj
        obj.x = new_x
        obj.y = new_y

    def clear(self, x: int, y: int):
        self.object_map[x][y] = None

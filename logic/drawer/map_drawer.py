import pygame
from pygame import Surface

from logic.drawer.image_repo import ImageRepo
from logic.game_map import GameMap
from logic.game_objects.army import Army
from logic.game_objects.game_object import GameObject


class MapDrawer:
    def __init__(self, game_map: GameMap, image_path, screen_width: int, screen_height: int, cell_size: int, screen: Surface):
        self.game_map = game_map
        self.image_repo = ImageRepo(image_path, cell_size)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size

        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def draw(self):
        for x in range(self.game_map.size_x):
            for y in range(self.game_map.size_y):
                field: GameObject = self.game_map.field_map[x][y]
                if field:
                    self._draw_cell(x, y, field)

                obj = self.game_map.army_map[x][y]
                if obj:
                    self._draw_army(x, y, obj)

    def _draw_cell(self, x: int, y: int, obj: GameObject):
        obj_image = self.image_repo.get_image(obj.get_image_path())
        coords = self._xy_to_coords(x, y)
        self.screen.blit(obj_image, coords)

    def _draw_army(self, x: int, y: int, obj: Army):
        obj_image = self.image_repo.get_image(obj.get_image_path())
        coords = self._xy_to_coords(x, y)
        self.screen.blit(obj_image, coords)
        size_surface = self.font.render(str(obj.size), True, (255, 0, 0))
        self.screen.blit(size_surface, coords)

    def _xy_to_coords(self, x: int, y: int):
        return x * self.cell_size, y * self.cell_size

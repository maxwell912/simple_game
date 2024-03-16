import pygame
from pygame.locals import *

from logic.drawer.map_drawer import MapDrawer
from logic.game_map import GameMap

# Инициализация Pygame
pygame.init()

# Размер экрана
screen_width = 800
screen_height = 800

map_width = 4
map_height = 4

# Размер клетки
cell_size = int(min(screen_width / map_width, screen_height / map_height))

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Передвижение кубика")

# Начальные координаты кубика
player_x = screen_width // 2
player_y = screen_height // 2

# Конечные координаты кубика
target_x = player_x
target_y = player_y

# Скорость перемещения кубика
speed = 5

# Основной цикл игры
running = True
clock = pygame.time.Clock()

game_map = GameMap(map_width, map_height)
map_drawer = MapDrawer(game_map, 'images', screen_width, screen_height, cell_size, screen)


while running:
    # Заполнение экрана белым цветом
    screen.fill((255, 255, 255))

    # Перемещение кубика к конечным координатам с плавностью
    if player_x != target_x:
        if player_x < target_x:
            player_x += speed
        else:
            player_x -= speed

    if player_y != target_y:
        if player_y < target_y:
            player_y += speed
        else:
            player_y -= speed

    map_drawer.draw()

    # Обновление экрана
    pygame.display.flip()

    # Проверка событий
    for event in pygame.event.get():
        can_move = target_x == player_x and target_y == player_y
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and can_move:
            if event.key == K_w:
                target_y -= cell_size
            elif event.key == K_s:
                target_y += cell_size
            elif event.key == K_a:
                target_x -= cell_size
            elif event.key == K_d:
                target_x += cell_size

    # Ограничение FPS
    clock.tick(60)

# Завершение Pygame
pygame.quit()
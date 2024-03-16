import pygame
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Размер экрана
screen_width = 800
screen_height = 800

# Размер клетки
cell_size = 100

# Загрузка изображения кубика
cube_image = pygame.image.load("images/cat.png")
cube_image = pygame.transform.scale(cube_image, (cell_size, cell_size))

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

    # Отрисовка кубика
    screen.blit(cube_image, (player_x, player_y))

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
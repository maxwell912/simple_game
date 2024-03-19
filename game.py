import pygame
from pygame.locals import *

from logic.drawer.map_drawer import MapDrawer
from logic.game_state import GameState, MakeIncome
from logic.maps.simple_map import Map1
from logic.player import Player, PlayerName
from logic.strategist import MyStrategist

# Инициализация Pygame
pygame.init()

# Размер экрана
screen_width = 900
screen_height = 500

player_1 = Player(PlayerName.RED)
player_2 = Player(PlayerName.BLUE)
bot = Player(PlayerName.GRAY)
game_map = Map1.create(player_1, player_2, bot)

map_width = game_map.size_x
map_height = game_map.size_y

# Размер клетки
cell_size = int(min(screen_width / map_width, screen_height / map_height))

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
map_drawer = MapDrawer(game_map, 'images', screen_width, screen_height, cell_size, screen)

game_state = GameState(game_map, [player_1, player_2], map_drawer)

strategist1 = MyStrategist(player_1)
strategist2 = MyStrategist(player_2)


while game_state.running:
    if game_state.day % 7 == 0:
        game_state.run_command(MakeIncome(game_state.game_map))

    game_state.make_moves(strategist1)
    game_state.make_moves(strategist2)

    # Проверка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            game_state.stop()

    game_state.end_day()


# Завершение Pygame
pygame.quit()
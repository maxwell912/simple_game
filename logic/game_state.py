import pygame

from logic.commands import *
from logic.drawer.map_drawer import MapDrawer
from logic.game_map import GameMap
from logic.player import Player
from logic.strategist import Strategist


class GameState:
    def __init__(self, game_map: GameMap, players: list[Player], map_drawer: MapDrawer):
        self.game_map = game_map
        self.players = players

        self.running = True

        self.day = 0
        self.clock = pygame.time.Clock()
        self.framerate = 10

        self.map_drawer = map_drawer

    def run_command(self, command: Command):
        if isinstance(command, MoveArmy):
            self.game_map.move_army(command.army, command.direction)
        elif isinstance(command, SpawnArmy):
            self.game_map.spawn_army(command.castle, command.size)

    def refresh(self):
        self.map_drawer.draw()
        # Обновление экрана
        pygame.display.flip()
        # Ограничение FPS
        self.clock.tick(self.framerate)

    def make_moves(self, strategist: Strategist):
        armies = self.game_map.get_armies(strategist.player)

        for army in armies:
            command = strategist.make_command(army, self.game_map)
            self.run_command(command)
            self.refresh()

        castles = self.game_map.get_castles(strategist.player)
        for castle in castles:
            command = strategist.make_command(castle, self.game_map)
            self.run_command(command)
            self.refresh()

    def end_day(self):
        self.day += 1

    def stop(self):
        self.running = False
from enum import Enum

from logic.game_objects.game_object import Location

class RoadDirection(Enum):
    dir02 = 0
    dir13 = 1
    dir01 = 2
    dir03 = 3
    dir12 = 4
    dir23 = 5
    dir013 = 6
    dir023 = 7
    dir123 = 8
    dir012 = 9
    dir0123 = 10

class Road(Location):

    def __init__(self, direction: RoadDirection):
        self.direction = direction


    def get_image_path(self) -> str:
        return 'doroga-' + str(self.direction.value) + '.png'

Road02 = Road(RoadDirection.dir02)
Road13 = Road(RoadDirection.dir13)
Road01 = Road(RoadDirection.dir01)
Road03 = Road(RoadDirection.dir03)
Road12 = Road(RoadDirection.dir12)
Road23 = Road(RoadDirection.dir23)
Road013 = Road(RoadDirection.dir013)
Road023 = Road(RoadDirection.dir023)
Road123 = Road(RoadDirection.dir123)
Road012 = Road(RoadDirection.dir012)
Road0123 = Road(RoadDirection.dir0123)

from logic.game_objects.game_object import GameObject


class Forest(GameObject):

    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    def get_image_path(self) -> str:
        return 'forest.png'

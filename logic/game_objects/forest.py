from logic.game_objects.game_object import GameObject


class Forest(GameObject):

    def get_image_path(self) -> str:
        return 'trava.png'

forest = Forest()
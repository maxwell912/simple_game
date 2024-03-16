from logic.player import Player


class GameObject:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_image_path(self) -> str:
        return ''


class Location(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    def handle_player(self, player: Player):
        if isinstance(self, HasPlayer):
            self.set_player(player)


class HasPlayer:
    def __init__(self, player: Player):
        self.player = player

    def set_player(self, new_player: Player):
        self.player = new_player


class MovableGameObject(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

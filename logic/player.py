class Player:
    START_GOLD = 1000
    player_num = 0

    def __init__(self):
        self.id = Player.player_num
        self.gold = Player.START_GOLD
        Player.player_num += 1

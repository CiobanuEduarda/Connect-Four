class Player:
    def __init__(self, player_name, chip):
        self.player_name = player_name
        self.chip = chip

    def get_name(self):
        return self.player_name

    def get_chip(self):
        return self.chip

    def __str__(self):
        return f"Player {self.player_name} is playing with {self.chip}!"

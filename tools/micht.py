from tools.deck import Deck


class Micht:
    def __init__(self):
        self.deck = Deck
        self.players = []

    def add_player(self, player):
        self.players.append(player)

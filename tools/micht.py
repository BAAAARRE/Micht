from tools.player import Player
from tools.deck import Deck


class Micht:
    def __init__(self):
        self.players = []
        self.nb_players = 0

    def register_player(self, player_name):
        player = Player(player_name)
        self.players.append(player)

    def update_nb_players(self):
        self.nb_players = len(self.players)

    def distribute_cards(self):
        full_cards = Deck.generate_cards(self.nb_players)
        print(full_cards)

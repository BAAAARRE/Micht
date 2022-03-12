from tools.player import Player
from tools.deck import Deck


class Micht:
    def __init__(self):
        self.players = []
        self.nb_players = 0
        self.liar = False
        self.current_call = ""
        self.last_player = ""
        self.last_player_cards = ""

    def register_player(self, player_name):
        player = Player(player_name)
        self.players.append(player)

    def update_nb_players(self):
        self.nb_players = len(self.players)

    def distribute_cards(self, nb_cards_to_distribute):
        full_cards = Deck.generate_cards(self.nb_players)
        sub_deck = [full_cards[i:i+nb_cards_to_distribute] for i in range(0, len(full_cards), nb_cards_to_distribute)]
        num_sub_deck = 0
        for player in self.players:
            for card in sub_deck[num_sub_deck]:
                player.add_card(card)
            num_sub_deck += 1

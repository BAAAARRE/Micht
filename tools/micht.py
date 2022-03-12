from tools.player import Player
from tools.deck import Deck


class Game:
    def __init__(self):
        self.players = []
        self.nb_players = int(input("Entrez le nombre de joueurs : "))
        self.nb_life = int(input("Nombre de vie par joueurs : "))

    def add_player(self, id, player_name):
        player = Player(id, player_name)
        self.players.append(player)

    def register_player(self):
        for num_player in range(self.nb_players):
            id_player = num_player + 1
            player_name = input(f"Ajouter le nom du joueur n°{id_player} : ")
            self.add_player(id_player, player_name, self.nb_life)


class Round(Game):
    def __init__(self):
        super().__init__()
        self.liar = False
        self.current_call = ""
        self.last_player = ""
        self.last_player_cards = ""

    def distribute_cards(self, nb_cards_to_distribute):
        full_cards = Deck.generate_cards(self.nb_players)
        sub_deck = [full_cards[i:i+nb_cards_to_distribute] for i in range(0, len(full_cards), nb_cards_to_distribute)]
        num_sub_deck = 0
        for player in self.players:
            for card in sub_deck[num_sub_deck]:
                player.add_card(card)
            num_sub_deck += 1


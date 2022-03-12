from tools.player import Player
from tools.deck import Deck


class Game:
    def __init__(self):
        self.players = []
        self.nb_players = int(input("Entrez le nombre de joueurs : "))
        self.nb_life = int(input("Nombre de vie par joueurs : "))

    def add_player(self, id, player_name, nb_life):
        player = Player(id, player_name, nb_life)
        self.players.append(player)

    def register_player(self):
        for num_player in range(self.nb_players):
            id_player = num_player + 1
            player_name = input(f"Ajouter le nom du joueur n°{id_player} : ")
            self.add_player(id_player, player_name, self.nb_life)

    def show_nb_life_player(self):
        for player in self.players:
            print(f"Il reste {player.nb_life} vie(s) à {player.name}")


class Round:
    def __init__(self, players, nb_cards_to_distribute):
        self.players = players
        self.nb_players = len(players)
        self.nb_cards_to_distribute = nb_cards_to_distribute
        self.liar = False
        self.current_call = ""
        self.last_player = ""
        self.last_player_cards = ""

    def distribute_cards(self, nb_cards_to_distribute):
        full_cards = Deck.generate_cards(self.nb_players)
        sub_deck = [full_cards[i:i + self.nb_cards_to_distribute] for i in
                    range(0, len(full_cards), self.nb_cards_to_distribute)]
        num_sub_deck = 0
        for player in self.players:
            player.reinitialize_cards()
            for card in sub_deck[num_sub_deck]:
                player.add_card(card)
            num_sub_deck += 1

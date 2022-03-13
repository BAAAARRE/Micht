from tools.player import Player
from tools.deck import Deck


class Game:
    def __init__(self):
        self.nb_players = int(input("Entrez le nombre de joueurs : "))
        self.nb_life = int(input("Nombre de vie par joueurs : "))
        self.players = []

    def add_player(self, id, player_name, nb_life):
        player = Player(id, player_name, nb_life)
        self.players.append(player)

    def register_player(self):
        for num_player in range(self.nb_players):
            id_player = num_player + 1
            player_name = input(f"Ajouter le nom du joueur n°{id_player} : ")
            self.add_player(id_player, player_name, self.nb_life)

    def remove_one_life(self, player_name):
        for player in self.players:
            if player.name == player_name:
                player.nb_life = player.nb_life - 1

    def check_if_one_player_is_dead(self):
        for player in self.players:
            if player.nb_life == 0:
                player_dead = player.name
                break
            else:
                player_dead = ""
        return player_dead

    def show_nb_life_player(self):
        for player in self.players:
            print(f"Il reste {player.nb_life} vie(s) à {player.name}")


class Round:
    def __init__(self, players, nb_cards_to_distribute):
        self.players = players
        self.nb_players = len(players)
        self.nb_cards_to_distribute = nb_cards_to_distribute
        self.distributed_cards = []
        self.liar = False
        self.current_call = ""
        self.last_player = ""

    def distribute_cards(self):
        full_cards = Deck.generate_cards(self.nb_players)
        sub_deck = [full_cards[i:i + self.nb_cards_to_distribute] for i in
                    range(0, len(full_cards), self.nb_cards_to_distribute)]
        num_sub_deck = 0
        for player in self.players:
            player.reinitialize_cards()
            for card in sub_deck[num_sub_deck]:
                player.add_card(card)
                self.distributed_cards.append(card)
            num_sub_deck += 1

    def game_round(self):
        self.distributed_cards = ", ".join([card.full_name for card in self.distributed_cards])
        while not self.liar:
            for player in self.players:
                player_cards = ", ".join([card.full_name for card in player.cards])
                print(f"C'est à {player.name} de jouer")
                ready_to_play = input("Tu es prêt à jouer? Appuis sur 'Entrée'")

                if ready_to_play == "":
                    print(f"\nTes cartes sont {player_cards}")

                    if len(self.current_call) == 0:
                        print(f"C'est à toi de faire le premier call")
                        self.current_call = input("Combinaison à call : ")
                        self.last_player = player.name
                        print("\n")

                    elif len(self.current_call) > 0:
                        print(f"{self.last_player} a call '{self.current_call}'")
                        liar_input = input("Est ce que c'est un menteur (Y/N)")

                        if liar_input == "Y":
                            print(
                                f"\n{self.last_player} a call '{self.current_call}' et il y avait {self.distributed_cards} dans le jeu"
                            )
                            self.liar = True
                            break

                        elif liar_input == "N":
                            print(f"C'est à toi de faire le call")
                            self.current_call = input("Combinaison à call : ")
                            self.last_player = player.name
                            print("\n")

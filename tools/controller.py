from tools.player import Player


class Controller:
    def __init__(self, game):
        self.game = game

    def register_player(self, player_name):
        # player_name = input("Entrez le nom d'un joueur ou appuyez sur 'Entréé' pour arreter l'ajout de joueur: ")
        if player_name.isalnum():
            player = Player(player_name)
            self.game.add_player(player)
        return not player_name.isalnum()

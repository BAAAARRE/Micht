from tools import micht, controller, viewer


def main():
    game = micht.Micht()

    game.register_player("Antoine")
    game.register_player("Florent")
    game.update_nb_players()

    print([player.name for player in game.players])
    print(game.nb_players)

    game.distribute_cards()


if __name__ == "__main__":
    main()

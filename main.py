from tools import micht


def main():
    game = micht.Game()
    game.register_player()

    num_game_round = 1
    while True:
        print(f"\n\n --- Partie n°{num_game_round} ---")
        game_round = micht.Round(game.players, 3)

        game_round.distribute_cards()
        game_round.game_round()
        player_name_to_remove_one_life = input("Entrez le nom du joueur qui a perdu : ")
        game.remove_one_life(player_name_to_remove_one_life)
        player_dead = game.check_if_one_player_is_dead()
        if len(player_dead) > 0:
            print(f"\nLa partie est fini, {player_dead} est mort")
            break
        else:
            pass

        game.show_nb_life_player()
        num_game_round += 1


if __name__ == "__main__":
    main()

from tools import micht


def main():
    game = micht.Micht()

    game.register_player("Antoine")
    game.register_player("Florent")
    game.register_player("Bagna")
    game.update_nb_players()
    game.distribute_cards(3)
    print("Le micht commence !")
    print("Les cartes ont été distribué\n")

    while not game.liar:
        for player in game.players:
            player_cards = ", ".join([card.full_name for card in player.cards])
            print(f"C'est à {player.name} de jouer")
            ready_to_play = input("Tu es prêt à jouer? Appuis sur 'Entrée'")

            if ready_to_play == "":
                print(f"Tes cartes sont {player_cards}")

                if len(game.current_call) == 0:
                    print(f"\nC'est à toi de faire le premier call")
                    game.current_call = input("Combinaison à call : ")
                    game.last_player = player.name
                    game.last_player_cards = player_cards
                    print("\n")

                elif len(game.current_call) > 0:
                    print(f"\n{game.last_player} a call '{game.current_call}'")
                    liar_input = input("Est ce que c'est un menteur (y/n)").lower()

                    if liar_input == "y":
                        print(f"{player.name} a call {game.current_call} et il avait {game.last_player_cards}")
                        game.liar = True
                        break

                    elif liar_input == "n":
                        print(f"\nC'est à toi de faire le call")
                        game.current_call = input("Combinaison à call : ")
                        game.last_player = player.name
                        game.last_player_cards = player_cards
                        print("\n")


if __name__ == "__main__":
    main()

def main():
    nb_players = input("Nombre de joueurs : ")
    for num_player in range(int(nb_players)):
        input(f"Nom du joueur n°{num_player + 1} : ")

if __name__ == "__main__":
    main()
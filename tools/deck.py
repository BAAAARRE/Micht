import random


class Card:
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.full_name = f"{name} de {suit}"


class Deck:
    def __init__(self, nb_players):
        self.list_cards = self.generate_cards()

    @staticmethod
    def generate_cards(nb_players):
        suits = ["Carreau", "Pique", "Coeur", "Trèfle"]
        names = ["Roi", "Reine", "Valet", "10", "9", "8", "7"]
        cards = []
        for name in names[:nb_players]:
            for suit in suits:
                card = Card(name, suit)
                cards.append(card)
        random.shuffle(cards)
        return cards

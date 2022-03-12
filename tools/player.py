class Player:
    def __init__(self, id, name, nb_life):
        self.id = id
        self.name = name
        self.nb_life = nb_life
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
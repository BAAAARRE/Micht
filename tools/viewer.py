class View:
    def __init__(self, game):
        self.game = game
        self.players = game.players

    def update(self):
        self.players = self.game.players

    def before_start_show(self):
        if len(self.players) > 0:
            print("The current players are: \n" + '\n'.join([player.name for player in self.players]))
        print("Time to add players, you must add at least two")

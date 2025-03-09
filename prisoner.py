class Prisoner:

    #initialize the prisoner with an empty history
    def __init__(self):
        self.history = []

    #abstract playing strategy
    def play(self, _):
        pass

    #needed to store history
    def update_history(self, move):
        self.history.append(move)

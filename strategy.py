from prisoner import Prisoner
from random import choice

class AlwaysCooperate(Prisoner):
    def play(self, _):
        return 'C'

class AlwaysDefect(Prisoner):
    def play(self, _):
        return 'D'

class TitForTat(Prisoner):
    def play(self, opponentsHistory):
        if not opponentsHistory:
            return choice(['C', 'D'])

        return opponentsHistory[-1]

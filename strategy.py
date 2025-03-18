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
            return 'C'

        return opponentsHistory[-1]

class GrimTrigger(Prisoner):
    def play(self, oppenentsHistory):
        if 'D' in oppenentsHistory:
            return 'D'
        else:
            return 'C'
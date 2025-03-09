from prisoner import Prisoner
from random import choice
import prisoner as prisoner
from strategy import AlwaysCooperate, AlwaysDefect, TitForTat

payoffValues = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (1, 1),
}

def playGame(numRounds):

    prisoners = []

    print("********** Game Start **********\n \nPrisoner Strategies")

    for i in range(2):
        #assign some strategy 
        prisoner = choice([AlwaysCooperate(), AlwaysDefect(), TitForTat()])
        prisoners.append(prisoner)
        print(f"Prisoner {i + 1}: {str(prisoner.__class__.__name__)}")

    pris1Score, pris2Score = 0, 0
    print("\n********** Rounds **********\n")
    for j in range(numRounds):
        #take info if needed for tit for tat
        move1 = prisoners[0].play(prisoners[1].history)
        move2 = prisoners[1].play(prisoners[0].history)

        #use matrix to find resulting vals
        payoff = payoffValues[(move1, move2)]
        pris1Score += payoff[0]
        pris2Score += payoff[1]

        # Update history
        prisoners[0].update_history(move1)
        prisoners[1].update_history(move2)

        print(f"Round {j+1}: {move1} vs {move2}\n\tPayoff: {payoff}\n")

    print(f"********* Final Score ********* \n\tPrisoner 1 = {pris1Score} \n\tPrisoner 2 = {pris2Score}")


playGame(10)
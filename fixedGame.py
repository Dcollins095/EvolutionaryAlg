from prisoner import Prisoner
from random import choice
import prisoner as prisoner
from strategy import AlwaysCooperate, AlwaysDefect, TitForTat, GrimTrigger
from fitnessEval import fitness

payoffMatrix = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (1, 1),
}

def playGame(numRounds):

    prisoners = []

    print("********** Game Start **********\n \nPrisoner Strategies")

    for i in range(2):
        # Randomly select a strategy and create an instance
        prisoner = choice([AlwaysCooperate(), AlwaysDefect(), TitForTat()])
        prisoners.append(prisoner)
        print(f"Prisoner {i + 1}: {str(prisoner.__class__.__name__)}")

    score1, score2 = 0, 0
    print("\n********** Rounds **********\n")
    for j in range(numRounds):
        move1 = prisoners[0].play(prisoners[1].history)
        move2 = prisoners[1].play(prisoners[0].history)

        # Get scores based on the payoff matrix
        payoff = payoffMatrix[(move1, move2)]
        score1 += payoff[0]
        score2 += payoff[1]

        # Update history
        prisoners[0].update_history(move1)
        prisoners[1].update_history(move2)

        print(f"Round {j+1}: {move1} vs {move2}\n\tPayoff: {payoff}")

    print(f"Final Score: \n\tPrisoner 1 = {score1} \n\tPrisoner 2 = {score2}")


def getFitness():
    print("\n********** Fitness Evaluation **********")
    strategies = [AlwaysCooperate(), AlwaysDefect(), TitForTat(), GrimTrigger()]
    for strategy in strategies:
        avgScore = fitness(strategy)
        print(f"{strategy.__class__.__name__} Average Score: {avgScore}")
    print("***************************************")

playGame(10)
getFitness()
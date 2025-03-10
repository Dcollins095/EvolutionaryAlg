from random import choice
import prisoner as prisoner
from strategy import AlwaysCooperate, AlwaysDefect, TitForTat, GrimTrigger

payoffValues = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (1, 1),
}

def fitness(strategy):

    fixedPrisoner = strategy
    numRounds = 10
    prisoners = []

    #print(f"\n********** Fitness for {strategy.__class__.__name__} **********")

    for s in strategies:
        #assign some strategy 
        prisoner = s
        prisoners.append(prisoner)

    totalScore = 0
    for prisoner in prisoners:
        fixedScore, pris2Score = 0, 0     
        #print(f"\n{fixedPrisoner.__class__.__name__} vs {prisoner.__class__.__name__}")
        for j in range(numRounds):
            
            #take info if needed for tit for tat
            move1 = fixedPrisoner.play(prisoner.history)
            move2 = prisoner.play(fixedPrisoner.history)

            #use matrix to find resulting vals
            payoff = payoffValues[(move1, move2)]
            fixedScore += payoff[0]
            totalScore += payoff[0]
            pris2Score += payoff[1]

            # Update history
            fixedPrisoner.update_history(move1)
            prisoner.update_history(move2)

        #print(f"{fixedScore}:{pris2Score}")
    #print(f"\nTotal Score: {totalScore}\nAverage Score: {totalScore/len(prisoners)}")

    return totalScore/len(prisoners)





global strategies
results = {}
strategies = [AlwaysCooperate(), AlwaysDefect(), TitForTat(), GrimTrigger()]
for strategy in strategies:
    avgScore = fitness(strategy)
    results[strategy.__class__.__name__] = avgScore

#print("\n********** Final Results **********")
#for strategy, score in results.items():
#    print(f"{strategy}: {score:.2f}")
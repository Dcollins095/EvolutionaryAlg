from random import choice, sample, random
from strategy import AlwaysCooperate, AlwaysDefect, TitForTat, GrimTrigger
from fitnessEval import payoffValues
from matplotlib import pyplot as plt

popSize = 100
generations = 50
tournamentSize = 5
mutation = 0.1
noise = 0.01
strats = [AlwaysCooperate, AlwaysDefect, TitForTat, GrimTrigger]
memorySize = 3

def initializePopulation():
    return [choice(strats)() for _ in range(popSize)]

def tournamentSelection(population, fitnessDict):
    tournament = sample(population, tournamentSize)
    best = max(tournament, key=lambda x: fitnessDict[x])
    return best

def mutate(strategy):
    if random() < mutation:
        return choice(strats)()
    return strategy

def applyNoise(move):
    if random() < noise:
        return 'C' if move == 'D' else 'D'
    return move

def coevolutionFitness(individual, population):
    totalScore = 0
    #for each individual in the pop
    for prisoner in population:
        if prisoner != individual:
            individual.history = []
            prisoner.history = []

            #multiple rounds
            for _ in range(memorySize):
                move1 = applyNoise(individual.play(prisoner.history))#moves with chance of noise
                move2 = applyNoise(prisoner.play(individual.history)) 
                payoff = payoffValues[(move1, move2)]#eval moves
                totalScore += payoff[0]
                individual.update_history(move1)#update history
                prisoner.update_history(move2)
    
    return totalScore

def evolve():
    population = initializePopulation()
    avgFitness = []
    totFitness = []
    
    for generation in range(generations):
        #Calculate Fitnss
        fitnessDict = {ind: coevolutionFitness(ind, population) for ind in population}
        
        #Calculate average and total fitness
        scores = sum(fitnessDict.values())
        avgFitness.append(scores / len(population))
        totFitness.append(scores)

        population = sorted(population, key=lambda x: fitnessDict[x], reverse=True)
        
        #Create a new population
        new_population = []
        for _ in range(popSize // 2):
            parent1 = tournamentSelection(population, fitnessDict)
            parent2 = tournamentSelection(population, fitnessDict)
            offspring1 = mutate(parent1)
            offspring2 = mutate(parent2)
            new_population.extend([offspring1, offspring2])
        
        population = new_population
    
    #final population
    print("\n=== Final Population ===")
    for individual in population:
        print(f"{individual.__class__.__name__}")

    #plot
    plt.figure(figsize=(10, 6))
    plt.plot(avgFitness, label='Average Fitness')
    plt.plot(totFitness, label='Total Fitness')
    plt.title('Fitness Progression over Generations')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.ylim(0)
    plt.legend()
    plt.grid()
    plt.show()

evolve()
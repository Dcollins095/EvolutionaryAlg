from random import choice, sample, random
from strategy import AlwaysCooperate, AlwaysDefect, TitForTat, GrimTrigger
from fitnessEval import fitness
from matplotlib import pyplot as plt

popSize = 100
generations = 50
tournamentSize = 5
mutation = 0.1
strats = [AlwaysCooperate, AlwaysDefect, TitForTat, GrimTrigger]


def initializePopulation():
    return [choice(strats)() for _ in range(popSize)]

def tournamentSelection(population):
    tournament = sample(population, tournamentSize)
    best = max(tournament, key=fitness)
    return best

def mutate(strategy):
    if random() < mutation:
        return choice(strats)()
    return strategy

def evolve():
    population = initializePopulation()
    
    fitnessDict = {}
    for ind in population:
            if ind not in fitnessDict:
                fitnessDict[ind.__class__.__name__] = fitness(ind)

    avgFitness = []
    totFitness = []    
    #print(f"Total Fitness: {score}")
    #print(f"Fitness Dict: {fitnessDict}")
    for generation in range(generations):
        #print(f"\n=== Generation {generation + 1} ===")
        
        scores = 0
        for p in population:
            scores += fitnessDict[p.__class__.__name__]

        avgFitness.append(scores / len(population))
        totFitness.append(scores)
        

        #selection and reproduction
        new_population = []
        for _ in range(popSize // 2):
            parent1 = tournamentSelection(population)
            parent2 = tournamentSelection(population)

            #no crossover—just copy parents and mutate
            offspring1 = mutate(parent1)
            offspring2 = mutate(parent2)

            new_population.extend([offspring1, offspring2])
        #new_population = new_population[:-10]
        #add random strategies maintaing diversity
        #new_population.extend([choice(strats)() for _ in range(10)])

        population = new_population
        #print(f"Population: {len(population)}")

    print("\n=== Final Population ===")
    for individual in population:
        print(f"{individual.__class__.__name__}")

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

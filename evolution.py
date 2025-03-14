from random import choice, sample, random
from strategy import AlwaysCooperate, AlwaysDefect, TitForTat, GrimTrigger
from fitnessEval import fitness
from matplotlib import pyplot as plt

popSize = 50
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
    
    bestFitness = []
    avgFitness = []
    for generation in range(generations):
        print(f"\n=== Generation {generation + 1} ===")

        #Evaluate fitness of each strategy
        scores = {ind: fitness(ind) for ind in population}

        #Sort population)
        population = sorted(population, key=lambda x: scores[x], reverse=True)
        bestFitness.append(scores[population[0]])
        avgFitness.append(sum(scores.values()) / len(scores))
        print("\nTop 5 Strategies:")
        for i in range(5):
            print(f"{population[i].__class__.__name__} - Fitness: {scores[population[i]]:.2f}")

        #selection and reproduction
        new_population = []
        for _ in range(popSize // 2):
            parent1 = tournamentSelection(population)
            parent2 = tournamentSelection(population)

            #no crossover—just copy parents and mutate
            offspring1 = mutate(parent1)
            offspring2 = mutate(parent2)

            new_population.extend([offspring1, offspring2])

        #add random strategies maintaing diversity
        while len(new_population) < popSize:
            new_population.append(choice(strats)())

        population = new_population

    print("\n=== Final Population ===")
    for individual in population:
        print(f"{individual.__class__.__name__}")

    plt.figure(figsize=(10, 6))
    plt.plot(bestFitness, label='Best Fitness')
    plt.plot(avgFitness, label='Average Fitness')
    plt.title('Fitness Progression over Generations')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.ylim(0)
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    evolve()

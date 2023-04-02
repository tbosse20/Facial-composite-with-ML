import numpy as np
import random
from enum import Enum


class Selection(Enum):
    Tournement = 0,
    Roulette = 1,


class Genetic:
    elitism = 0.00
    newComer = 0.00
    mutation = 0.05
    lowerCut = 0.00
    tourSize = 4

    def __init__(self, unitType, selection, populationSize):
        self.unitType = unitType  # Population unit type
        self.selection = selection  # Parent selection method

        self.population = self.Populate(populationSize)  # Initialize population

    # Generate population from given or random DNA
    def Populate(self, populationSize):

        # Loop to fit populationSize
        population = [
            self.unitType()  # Birth child
            for i in range(populationSize)
        ]

        return population  # Return made population

    def SelectParents(self):

        match self.selection:
            case Selection.Tournement:
                return self.TournamentSelection()
            case self.selection:
                return self.RouletteSelection()

    # Pick parents by random and set them up in a tournament
    def TournamentSelection(self):
        parents = []  # Collect winner parents

        # Iterate for two parents
        for i in range(2):

            fightingParents = []  # Picked parents

            # Pick random parents to fight each other
            while len(fightingParents) < self.tourSize:
                randomParentIndex = random.randint(0, len(self.population) - 1)  # Random parent index
                parent = self.population[randomParentIndex]  # Get parent from population
                if parent in fightingParents: continue  # Already picked, new parent
                fightingParents.append(parent)  # Append to picked parents

            # The parent with the best score wins
            winningParent = max(fightingParents, key=lambda x: x.fitness)
            parents.append(winningParent)  # Append winner parent to winner couple

        return parents  # Pair of parents

    # Pick parents by chance depending on their fitness score
    def RouletteSelection(self):
        # Get all fitness scores
        fitness = [
            parent.fitness()  # Append parents fitness
            for parent in selcParts  # Loop all parents
        ]

        # TODO: Test
        # Pick two parents by random, but depended on their fitness as chance
        flipFit = np.subtract(max(fitness), fitness)  # Invert fitness scores
        normFit = np.divide(flipFit, sum(flipFit))  # "Normalize" invert fitness
        couple = np.random.choice(selcParts, 2, p=normFit)  # Weight random parent

        return couple  # Pair of parents

    # Elitism - Get the best parents selected independent
    def Elitism(self):
        if random.random > self.newComer: return

        sortedPopulation = sorted(
            self.population,
            key=lambda x: x.get_fitness(),
            reverse=True)

    # Newcomer - completely new DNAs
    def NewComer(self):
        if random.random > self.newComer: return

    def LowerCut(self):
        pass
        # Remove worst scored parents
        # lowerCutIndex = int(len(population) * self.lowerCut)
        # population = population[:lowerCutIndex]  # Select parents

    def ProduceOffsprings(self, parents):
        DNAs = self.Crossover(parents)  # Crossover parents DNA
        # DNAs = self.Mutate(DNAs)  # Mutate DNAs

        # Convert DNAs to new units
        offsprings = [
            self.unitType(DNA)
            for DNA in DNAs
        ]

        return offsprings

    # Crossover DNA from two parents to make new child DNA
    def Crossover(self, parents):
        randomHalfDNA = random.randint(0, len(parents[0].DNA))

        twins = []
        for i in range(2):
            DNA = parents[i].DNA
            firstHalf = dict(list(DNA.items())[:randomHalfDNA])  # Second half of DNA

            DNA = parents[(1 - i)].DNA
            secondHalf = dict(list(DNA.items())[randomHalfDNA:])

            childDNA = {**firstHalf, **secondHalf}  # Add two DNA parts together
            twins.append(childDNA)  # Append to children DNA

        return twins  # return twins DNA

    # Mutation in DNA string
    def Mutate(self, offsprings):

        # Loop all children DNA
        for i, offspring in enumerate(offsprings):

            # Loop all "bytes" in child DNA
            for j, values in enumerate(offspring.DNA.items()):

                # Make new "byte", prob. being mutated
                for k, DNAByte in enumerate(childDNA[parameter]):  # Loop all bits in "byte"

                    updatedDNAByte = [
                        str(1 - int(DNABit))  # Swap bit
                        if ((DNABit != "-" and k != 0) and random.random() <= self.mutation)
                        else DNABit
                        for DNABit in DNAByte
                    ]

                    updatedDNAByte = "".join(updatedDNAByte)
                    childrenDNA[i][parameter][k] = updatedDNAByte  # Update "byte"

        return offsprings  # Mutated children DNA

    # Fit a beam using genetic algorithm
    def Evolve(self, n):

        # Loop population until children is same size
        nextGeneration = list()

        # Loop until children DNA list is as big as original population
        while len(nextGeneration) < len(self.population):
            # Pick parents with selected selection method
            parents = self.SelectParents()

            nextGeneration += self.ProduceOffsprings(parents)

        return nextGeneration

    def __str__(self):
        for unit in self.population:
            print(unit)
        return ""


class Test:
    def __init__(self, DNA=None):
        self.fitness = 1
        if DNA == None:
            DNA = {
                "length": random.randint(1, 5),
                "width": random.randint(1, 7),
                "height": random.randint(1, 12),
                "weight": random.randint(1, 12),
                "ratio": random.randint(1, 12),
                "size": random.randint(1, 12),
            }
        self.DNA = DNA

    def __str__(self):
        return str(self.DNA)


if __name__ == "__main__":
    genetic = Genetic(
        Test,
        Selection.Tournement,
        10
    )
    print(genetic)
    genetic.Evolve(5)
    print(genetic)

import Genetic
import FacialComposit

genetic = Genetic.Genetic(
selection = Genetic.Selection.Tournement,
unitType = FacialComposit.Face
populationSize = 100
)

while True:

    FacialComposit.display(genetic.population)
    genetic.evolve(1)

# Genetic.py
# def evolve(n=1):
# self.selection
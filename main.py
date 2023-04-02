import Genetic
import FacialComposit

genetic = Genetic.Genetic(Genetic.select.tournememt)
genetic.unit(FacialComposit.Face)
genetic.populate(100)

while True:

    FacialComposit.display(genetic.population)
    genetic.evolve(1)
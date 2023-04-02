import Genetic
import FacialComposit

genetic = Genetic.Genetic(Genetic.select.tournememt)
genetic.unit(FacialComposit.Face)
population = genetic.populate(100)

while True:

    FacialComposit.display(population)
    genetic.evolve(1)
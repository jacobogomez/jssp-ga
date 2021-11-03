from jssp_ga import jssp_instance, scheduler
from jssp_ga.genetic_algorithm.operators import initial_population


class Population:
    def __init__(self, jssp_instance, population_size, empty=False):
        if not empty:
            self.individuals = initial_population.generate_random_population(
                jssp_instance, population_size
            )
        else:
            self.individuals = []

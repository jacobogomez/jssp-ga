import copy
import random
import tempfile
import time

from jssp_ga import file_helper, scheduler
from jssp_ga.genetic_algorithm import fitness, population
from jssp_ga.genetic_algorithm.operators import crossover, mutation, selection


def my_ga(instance):
    t1 = time.time()
    random.seed(1)

    tmp = tempfile.NamedTemporaryFile()
    with open(tmp.name, "w") as f:
        f.write(instance)

    JSSP_INSTANCE = file_helper.load_instance(tmp.name)
    POPULATION_SIZE = 200
    GENERATIONS = 550
    CROSSOVER_RATE = 0.95
    MUTATION_PROBABILITY = 0.15

    ga_population = population.Population(JSSP_INSTANCE, POPULATION_SIZE)

    for i in range(GENERATIONS):
        for individual in ga_population.individuals:
            fitness.calculate_fitness(individual, JSSP_INSTANCE)

        ga_population.individuals = sorted(
            ga_population.individuals, key=lambda i: i["data"][1]
        )
        for i in range(len(ga_population.individuals)):
            ga_population.individuals[i]["id"] = i

        new_population = population.Population(
            JSSP_INSTANCE, POPULATION_SIZE, empty=True
        )

        while len(new_population.individuals) <= POPULATION_SIZE:
            first_parent_id = selection.roulette_selection(ga_population)
            second_parent_id = selection.roulette_selection(ga_population)
            crossover_probability = random.random()
            if crossover_probability > CROSSOVER_RATE:
                first_offspring, second_offspring = crossover.crossover(
                    ga_population.individuals[first_parent_id],
                    ga_population.individuals[second_parent_id],
                    JSSP_INSTANCE,
                )
                new_population.individuals.append(
                    {"id": None, "data": [first_offspring, None]}
                )
                new_population.individuals.append(
                    {"id": None, "data": [second_offspring, None]}
                )
            else:
                new_population.individuals.append(
                    {
                        "id": None,
                        "data": [
                            (ga_population.individuals[first_parent_id])["data"][0],
                            None,
                        ],
                    }
                )
                new_population.individuals.append(
                    {
                        "id": None,
                        "data": [
                            (ga_population.individuals[second_parent_id])["data"][0],
                            None,
                        ],
                    }
                )

        for individual in new_population.individuals:
            mutate = random.random()
            if mutate > MUTATION_PROBABILITY:
                individual["data"][0] = mutation.mutation(individual, JSSP_INSTANCE)

        new_population.individuals.append(ga_population.individuals[-1])

        while len(new_population.individuals) > POPULATION_SIZE:
            new_population.individuals.pop(0)

        ga_population = copy.deepcopy(new_population)

    for individual in ga_population.individuals:
        fitness.calculate_fitness(individual, JSSP_INSTANCE)
    ga_population.individuals = sorted(
        ga_population.individuals, key=lambda i: i["data"][1]
    )
    for i in range(len(ga_population.individuals)):
        ga_population.individuals[i]["id"] = i

    best = ga_population.individuals[-1]
    best_schedule = scheduler.Schedule(best["data"][0], JSSP_INSTANCE)
    t2 = time.time()
    t = t2 - t1

    solution = {
        "best": best_schedule.schedule,
        "makespan": best_schedule.calculate_makespan(),
        "time": t,
    }

    return solution

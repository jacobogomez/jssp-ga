import itertools
import random

from jssp_ga import jssp_instance, scheduler
from jssp_ga.genetic_algorithm import fitness, population


def get_random_individual(jssp_instance):
    individual = []
    for column in range(jssp_instance.number_of_machines):
        column_values = [row[column] for row in jssp_instance.list_of_tuples]
        random.shuffle(column_values)
        individual.append(column_values)
    individual = list(itertools.chain(*individual))
    return individual


def generate_random_population(jssp_instance, population_size):
    individuals = []
    for _ in range(population_size):
        individual = {
            "id": _,
            "data": [get_random_individual(jssp_instance), None],
        }
        individuals.append(individual)
    return individuals


def set_worst_individual(jssp_instance):
    individual = []
    for column in range(jssp_instance.number_of_machines):
        column_values = [row[column] for row in jssp_instance.list_of_tuples]
        individual.append(column_values)
    individual = list(itertools.chain(*individual))
    worst_schedule = scheduler.Schedule(individual, jssp_instance)
    worst_makespan = worst_schedule.add_all_durations()
    worst_individual = {
        "id": -1,
        "data": [individual, 1 / worst_makespan],
    }
    return worst_individual

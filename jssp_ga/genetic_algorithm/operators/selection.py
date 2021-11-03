import random

from jssp_ga.genetic_algorithm import population


def sum_all_fitness(population):
    total_fitness = 0
    for individual in population.individuals:
        total_fitness += individual["data"][1]
    return total_fitness


def get_individual_probability(population):
    total_fitness = sum_all_fitness(population)
    cumulative_probability = 0
    probabilities = []
    for individual in population.individuals:
        relative_fitness = individual["data"][1] / total_fitness
        probability = {
            "id": individual["id"],
            "probability": cumulative_probability + relative_fitness,
        }
        cumulative_probability += relative_fitness
        probabilities.append(probability)
    return probabilities


def roulette_selection(population):
    probabilities = get_individual_probability(population)
    random_probability = random.random()
    for individual in probabilities:
        if individual["probability"] > random_probability:
            return individual["id"]

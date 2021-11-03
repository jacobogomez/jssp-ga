from jssp_ga import scheduler


def calculate_fitness(individual, jssp_instance):
    individual_schedule = scheduler.Schedule(individual["data"][0], jssp_instance)
    fitness = 1 / individual_schedule.calculate_makespan()
    individual["data"][1] = fitness

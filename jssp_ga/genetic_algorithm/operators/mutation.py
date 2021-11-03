from random import randint, sample

from jssp_ga.scheduler import Schedule

JOBS_TO_SWAP = 2


def mutation(individual, jssp_instance):
    # To apply the mutation operator, a machine is chosen randomly.
    individual_data = individual["data"][0]
    individual_schedule = Schedule(individual_data, jssp_instance)
    random_machine_number = randint(0, jssp_instance.number_of_machines - 1)
    # Then two consecutive jobs
    # are chosen randomly on this machine. While maintaining the task precedence relation, the position of the two
    # jobs is swapped. Swapping is done only once for the
    # whole schedule.
    jobs_to_swap = get_swappable_jobs(individual_data, random_machine_number)
    mutated_individual = []
    for task in individual_data:
        candidate_task = task
        if task == jobs_to_swap[0]:
            candidate_task = jobs_to_swap[1]
        if task == jobs_to_swap[1]:
            candidate_task = jobs_to_swap[0]
        if candidate_task not in mutated_individual:
            preceeding_task = individual_schedule.decomposed_tasks.get(candidate_task)[
                "precedence"
            ]
            if (
                preceeding_task is not None
                and preceeding_task not in mutated_individual
            ):
                mutated_individual.append(preceeding_task)
            mutated_individual.append(candidate_task)
    return mutated_individual


def get_swappable_jobs(individual_data, machine_number):
    jobs_to_swap = []
    jobs_from_machine_number = [
        job for job in individual_data if job[1] == machine_number
    ]
    [omg_job] = sample(jobs_from_machine_number, 1)
    first_job_index = jobs_from_machine_number.index(omg_job)
    if first_job_index == len(jobs_from_machine_number) - 1:
        jobs_to_swap.append(jobs_from_machine_number[first_job_index - 1])
        jobs_to_swap.append(jobs_from_machine_number[first_job_index])
    else:
        jobs_to_swap.append(jobs_from_machine_number[first_job_index])
        jobs_to_swap.append(jobs_from_machine_number[first_job_index + 1])

    return jobs_to_swap

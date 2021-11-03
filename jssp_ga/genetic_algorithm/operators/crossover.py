from random import randint, sample

from jssp_ga import scheduler


def crossover(first_parent, second_parent, jssp_instance):
    first_parent_data = first_parent["data"][0]
    second_parent_data = second_parent["data"][0]
    # 1. Given a problem instance with n jobs and m machines, randomly select a
    # number i, (where i ∈ 1, 2,..., n − 1).
    number_of_random_jobs = randint(1, jssp_instance.number_of_jobs - 1)
    # 2. Next, randomly select i jobs which are the jobs to
    # be passed on from parent to offspring per parent.
    list_of_jobs = range(jssp_instance.number_of_jobs)
    first_parent_sample = list(sample(list_of_jobs, number_of_random_jobs))
    second_parent_sample = list(sample(list_of_jobs, number_of_random_jobs))
    # 3. Create a mask pattern with only zeros of maximum
    # length equal to n × m.
    first_parent_mask = [0 for task in first_parent_data]
    second_parent_mask = [0 for task in second_parent_data]
    # 4. For each task of each job selected in Step 2, flip the
    # bit from a 0 to 1, at each corresponding location of
    # the task in the respective mask pattern.
    # TODO(@jacobogomez) Extract this to a function
    for i in range(len(first_parent_data)):
        if first_parent_data[i][0] in first_parent_sample:
            first_parent_mask[i] = 1
    for i in range(len(second_parent_data)):
        if second_parent_data[i][0] in second_parent_sample:
            second_parent_mask[i] = 1
    # 5. While maintaining the task precedence order from
    # P1, all the tasks whose position correspond to a 1,
    # in the mask pattern are copied (from left to right) to
    # offspring, C1.
    first_offspring = [None for task in first_parent_data]
    for i in range(len(first_parent_mask)):
        if first_parent_mask[i] == 1:
            first_offspring[i] = first_parent_data[i]

    second_offspring = [None for task in second_parent_data]
    for i in range(len(second_parent_mask)):
        if second_parent_mask[i] == 1:
            second_offspring[i] = second_parent_data[i]
    # 6. The remaining tasks in C1 are copied from the other
    # parent, P2 (tasks already in C1 are not copied from
    # parent P2)
    for i in range(len(second_parent_data)):
        for j in range(len(first_offspring)):
            if second_parent_data[i] not in first_offspring:
                if first_offspring[j] is None:
                    first_offspring[j] = second_parent_data[i]
                    break

    for i in range(len(first_parent_data)):
        for j in range(len(second_offspring)):
            if first_parent_data[i] not in second_offspring:
                if second_offspring[j] is None:
                    second_offspring[j] = first_parent_data[i]
                    break

    return first_offspring, second_offspring

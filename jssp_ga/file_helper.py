from jssp_ga import jssp_instance


def load_instance(file):
    with open(file) as f:
        name = f.readline()
        number_of_machines = int(f.readline().split()[1])
        jobs = []
        for line in f:
            line = line.split()
            number_of_tasks = len(line) // 2
            job = []
            for i in range(number_of_tasks):
                machine_id = int(line[i * 2])
                operation_time = int(line[i * 2 + 1])
                operation = {
                    "machine_id": machine_id,
                    "duration": operation_time,
                }
                job.append(operation)
            jobs.append(job)
        return jssp_instance.JSSPInstance(name, jobs, number_of_machines)

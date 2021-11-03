class JSSPInstance:
    def __init__(self, name, jobs, number_of_machines):
        self.name = name
        self.jobs = jobs
        self.number_of_jobs = len(jobs)
        self.number_of_machines = number_of_machines
        self.list_of_tuples = self.to_list_of_tuples()

    def __getitem__(self, index):
        return self.jobs[index]

    def __len__(self):
        return self.number_of_jobs

    def to_list_of_tuples(self):
        jssp_list = []
        for job in range(self.number_of_jobs):
            operation_list = []
            for operation in self.jobs[job]:
                job_machine = (job, operation["machine_id"])
                operation_list.append(job_machine)
            jssp_list.append(operation_list)
        return jssp_list

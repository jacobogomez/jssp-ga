from jssp_ga import jssp_instance


class Schedule:
    def __init__(self, schedule, jssp_instance):
        self.schedule = schedule
        self.decomposed_tasks = self.decompose_tasks(jssp_instance)
        self.task_durations = {}
        self.get_task_times()

    def __getitem__(self, index):
        return self.decomposed_tasks[self.schedule[index]]

    def decompose_tasks(self, jssp_instance):
        decomposed_tasks = {}
        for job in range(len(jssp_instance)):
            for task in range(jssp_instance.number_of_machines):
                current_task = jssp_instance[job][task]
                preceeding_task = jssp_instance[job][task - 1]
                job_machine_id = (job, current_task["machine_id"])
                task_duration = current_task["duration"]
                precedence = (job, preceeding_task["machine_id"])
                if task == 0:
                    precedence = None
                decomposed_task = {
                    "duration": task_duration,
                    "precedence": precedence,
                }
                decomposed_tasks[job_machine_id] = decomposed_task
        return decomposed_tasks

    def get_preceeding_task(self, task):
        if self.decomposed_tasks[task]["precedence"] is None:
            return (-1, -1)
        else:
            return self.decomposed_tasks[task]["precedence"]

    def check_task_in_progress(self, task):
        if task not in self.task_durations:
            return {
                "start_time": 0,
                "duration": 0,
                "end_time": 0,
            }
        else:
            return self.task_durations[task]

    def check_busy_machine(self, machine_id):
        keys = [key for key in self.task_durations if key[1] == machine_id]
        if not keys:
            return [
                {
                    "start_time": 0,
                    "duration": 0,
                    "end_time": 0,
                }
            ]
        else:
            return [self.task_durations[key] for key in keys]

    def get_last_machine_end_time(self, machine_tasks):
        return max(task["end_time"] for task in machine_tasks)

    def add_all_durations(self):
        max_makespan = 0
        for task in self.decomposed_tasks:
            max_makespan += self.decomposed_tasks[task]["duration"]
        return max_makespan

    def get_task_times(self):
        self.task_durations[self.schedule[0]] = {
            "start_time": 0,
            "duration": self[0]["duration"],
            "end_time": 0 + self[0]["duration"],
        }
        for task in range(1, len(self.schedule)):
            preceeding_task = self.get_preceeding_task(self.schedule[task])
            preceeding_task_end_time = self.check_task_in_progress(preceeding_task)[
                "end_time"
            ]
            same_machine_jobs = self.check_busy_machine(self.schedule[task][1])
            same_machine_last_end_time = self.get_last_machine_end_time(
                same_machine_jobs
            )
            new_start_time = max(preceeding_task_end_time, same_machine_last_end_time)
            task_duration = self[task]["duration"]
            self.task_durations[self.schedule[task]] = {
                "start_time": new_start_time,
                "duration": task_duration,
                "end_time": new_start_time + task_duration,
            }

    def calculate_makespan(self):
        return max(
            self.task_durations[key]["end_time"] for key in self.task_durations.keys()
        )

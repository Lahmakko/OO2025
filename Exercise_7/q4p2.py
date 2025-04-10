class Task:
    def __init__(self, description, programmer, workload):
        self.id = id(self)  # Unique identifier for each task
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def mark_finished(self):
        self.finished = True

    def is_finished(self):
        return self.finished

    def __repr__(self):
        status = 'Finished' if self.is_finished() else 'Unfinished'
        return f"Task(id={self.id}, description='{self.description}', programmer='{self.programmer}', workload={self.workload}, status='{status}')"


class OrderBook:
    def __init__(self):
        self.tasks = []

    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self.tasks.append(task)

    def all_orders(self):
        return self.tasks

    def programmers(self):
        return list(set(task.programmer for task in self.tasks))

    def mark_finished(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_finished()
                return
        raise ValueError(f"No task found with id {task_id}")

    def finished_orders(self):
        return [task for task in self.tasks if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self.tasks if not task.is_finished()]

    def status_of_programmer(self, programmer):
        finished = [task for task in self.tasks if task.programmer == programmer and task.is_finished()]
        unfinished = [task for task in self.tasks if task.programmer == programmer and not task.is_finished()]
        return {
            'programmer': programmer,
            'finished': finished,
            'unfinished': unfinished
        }

    def __repr__(self):
        return f"OrderBook(tasks={self.tasks})"

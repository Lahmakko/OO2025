class Task:
    _id_counter = 1

    def __init__(self, description, programmer, workload):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

# Example usage:
if __name__ == "__main__":
    task1 = Task("program hello world", "Eric", 3)
    task2 = Task("program webstore", "Adele", 10)
    task3 = Task("program mobile app", "Eric", 25)
    print(task1)
    task1.mark_finished()
    print(task1)
    print(task2)
    print(task3)

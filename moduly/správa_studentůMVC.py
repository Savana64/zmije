class Model:

    def __init__(self):
        # Initialize an empty list to hold tasks.
        self.tasks = []
    # Adds a task to the list of tasks.
    def add_task(self, task):
        self.tasks.append(task)
    # Returns the list of tasks.
    def get_tasks(self):
        return self.tasks

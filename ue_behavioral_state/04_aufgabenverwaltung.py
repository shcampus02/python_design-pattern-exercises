"""
Übung 4 - Aufgabenverwaltung

In dieser Übung haben Sie eine Aufgabe, die verschiedene Zustände durchlaufen kann, z.B. neu, in Bearbeitung und abgeschlossen.

Implementieren Sie die Klassen 'TaskState', 'NewTaskState', 'InProgressTaskState', 'CompletedTaskState' und 'Task'.
"""


class TaskState:
    pass


class NewTaskState(TaskState):
    pass


class InProgressTaskState(TaskState):
    pass


class CompletedTaskState(TaskState):
    pass


class Task:
    pass


if __name__ == "__main__":
    task = Task()
    task.advance_state()
    print(task.get_state())  # Output: NewTaskState
    task.advance_state()
    print(task.get_state())  # Output: InProgressTaskState
    task.advance_state()
    print(task.get_state())  # Output: CompletedTaskState
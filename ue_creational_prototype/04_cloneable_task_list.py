# Implement a TaskList class with deep cloning capability that includes a list of tasks and a project name.
# Ensure that the list of tasks can be independently modified in clones.




if __name__ == '__main__':
    original_task_list = TaskList("Project Phoenix", ["Task 1", "Task 2"])
    print(original_task_list)  # Project Phoenix: Task 1, Task 2

    cloned_task_list = original_task_list.clone()
    cloned_task_list.tasks.append("Task 3")
    print(original_task_list)  # Should not include "Task 3"
    print(cloned_task_list)    # Should include "Task 3"

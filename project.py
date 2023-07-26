# project

tasks = []


def main():
    print("Welcome to the Task Manager!")
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            complete_task()
        elif choice == 4:
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


def add_task():
    print("\nAdd a new task:")
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    task_due_date = input("Enter due date (YYYY-MM-DD): ")

    task = {
        "name": task_name,
        "description": task_description,
        "due_date": task_due_date,
        "completed": False,
    }

    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTask List:")
        for index, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(
                f"{index}. {task['name']} - {task['description']} (Due Date: {task['due_date']}) [{status}]"
            )


def complete_task():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTask List:")
        for index, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(
                f"{index}. {task['name']} - {task['description']} (Due Date: {task['due_date']}) [{status}]"
            )

        task_number = int(
            input("Enter the number of the task you want to mark as completed: ")
        )

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number. Please try again.")


if __name__ == "__main__":
    main()

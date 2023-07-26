import os
from datetime import datetime

tasks = []


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def add_task():
    clear_screen()
    print("\033[92m\nAdd a new task:\033[0m")  # Verde claro
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")

    while True:
        task_due_date = input("Enter due date (YYYY-MM-DD): ")
        if validate_date(task_due_date):
            break
        else:
            print("\033[91mInvalid date format. Please try again.\033[0m")  # Vermelho claro

    task = {
        "name": task_name,
        "description": task_description,
        "due_date": task_due_date,
        "completed": False,
    }

    tasks.append(task)
    print("\033[92mTask added successfully!\033[0m")  # Verde claro
    input("\nPress enter to continue...")


def view_tasks():
    clear_screen()
    if not tasks:
        print("\033[91mNo tasks found.\033[0m")  # Vermelho claro
    else:
        print("\033[92m\nTask List:\033[0m")  # Verde claro
        for index, task in enumerate(tasks, 1):
            status = "\033[92mCompleted\033[0m" if task["completed"] else "\033[91mNot Completed\033[0m"  # Verde claro se completada, Vermelho claro se não completada
            print(
                f"{index}. {task['name']} - {task['description']} (Due Date: {task['due_date']}) [{status}]"
            )
    input("\nPress enter to continue...")


def complete_task():
    clear_screen()
    if not tasks:
        print("\033[91mNo tasks found.\033[0m")  # Vermelho claro
    else:
        print("\033[92m\nTask List:\033[0m")  # Verde claro
        for index, task in enumerate(tasks, 1):
            status = "\033[92mCompleted\033[0m" if task["completed"] else "\033[91mNot Completed\033[0m"  # Verde claro se completada, Vermelho claro se não completada
            print(
                f"{index}. {task['name']} - {task['description']} (Due Date: {task['due_date']}) [{status}]"
            )

        while True:
            task_number = int(
                input("Enter the number of the task you want to mark as completed: ")
            )

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("\033[92mTask marked as completed.\033[0m")  # Verde claro
                break
            else:
                print("\033[91mInvalid task number. Please try again.\033[0m")  # Vermelho claro
    input("\nPress enter to continue...")


def main():
    clear_screen()
    print("\033[95mWelcome to the Task Manager!\033[0m")  # Roxo claro
    input("\nPress enter to continue...")

    while True:
        clear_screen()
        print("\033[93m\nMenu:\033[0m")  # Amarelo claro
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        while True:
            try:
                choice = int(input("Enter your choice (1/2/3/4): "))
                if 1 <= choice <= 4:
                    break
                else:
                    print("\033[91mInvalid choice. Please try again.\033[0m")  # Vermelho claro
            except ValueError:
                print("\033[91mInvalid choice. Please enter a number.\033[0m")  # Vermelho claro

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            complete_task()
        elif choice == 4:
            print("\033[93mExiting Task Manager.\033[0m")  # Amarelo claro
            break


if __name__ == "__main__":
    main()

# test_project
from project import add_task, view_tasks, complete_task, tasks

def test_add_task():

    add_task()
    assert len(tasks) == 1
    assert tasks[0]["name"] == "Task 1"
    assert tasks[0]["description"] == "Description for Task 1"
    assert tasks[0]["due_date"] == "2023-07-15"
    assert tasks[0]["completed"] is False

def test_view_tasks_empty():

    view_tasks()
    assert "No tasks found." in capsys.readouterr().out

def test_view_tasks():

    tasks.clear()
    tasks.append({"name": "Task 1", "description": "Description for Task 1", "due_date": "2023-07-15", "completed": False})
    tasks.append({"name": "Task 2", "description": "Description for Task 2", "due_date": "2023-07-16", "completed": True})

    view_tasks_output = capsys.readouterr().out
    assert "Task List:" in view_tasks_output
    assert "1. Task 1 - Description for Task 1 (Due Date: 2023-07-15) [Not Completed]" in view_tasks_output
    assert "2. Task 2 - Description for Task 2 (Due Date: 2023-07-16) [Completed]" in view_tasks_output

def test_complete_task():

    tasks.clear()
    tasks.append({"name": "Task 1", "description": "Description for Task 1", "due_date": "2023-07-15", "completed": False})
    tasks.append({"name": "Task 2", "description": "Description for Task 2", "due_date": "2023-07-16", "completed": True})

    complete_task()
    assert tasks[1]["completed"] is False

def test_complete_task_invalid_input():

    tasks.clear()
    tasks.append({"name": "Task 1", "description": "Description for Task 1", "due_date": "2023-07-15", "completed": False})


    with pytest.raises(ValueError):
        input_values = ["0"]
        input_mock = lambda _: input_values.pop(0)
        builtin_input_mock = "__builtin__.input" if sys.version_info.major < 3 else "builtins.input"

        with patch(builtin_input_mock, input_mock):
            complete_task()

    
    assert tasks[0]["completed"] is False

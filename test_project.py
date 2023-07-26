from unittest.mock import patch

import pytest

from project import tasks, add_task, view_tasks, complete_task


def test_add_task():
    tasks.clear()  # Limpar a lista de tarefas no início do teste
    with patch('builtins.input', side_effect=["Task 1", "Description for Task 1", "2023-07-15", ""]):
        add_task()
    assert len(tasks) == 1
    assert tasks[0]["name"] == "Task 1"
    assert tasks[0]["description"] == "Description for Task 1"
    assert tasks[0]["due_date"] == "2023-07-15"
    assert tasks[0]["completed"] is False


def test_view_tasks_empty(capsys):
    tasks.clear()  # Limpar a lista de tarefas no início do teste
    with patch('builtins.input', return_value=''):
        view_tasks()
    captured = capsys.readouterr()
    assert "No tasks found." in captured.out


def test_view_tasks(capsys):
    tasks.clear()  # Limpar a lista de tarefas no início do teste
    tasks.append({"name": "Task 1", "description": "Description for Task 1", "due_date": "2023-07-15", "completed": False})
    tasks.append({"name": "Task 2", "description": "Description for Task 2", "due_date": "2023-07-16", "completed": True})

    with patch('builtins.input', return_value=''):
        view_tasks()

    view_tasks_output = capsys.readouterr().out
    assert "\033[92m\nTask List:\033[0m" in view_tasks_output
    assert f"1. Task 1 - Description for Task 1 (Due Date: 2023-07-15) [\033[91mNot Completed\033[0m]" in view_tasks_output
    assert f"2. Task 2 - Description for Task 2 (Due Date: 2023-07-16) [\033[92mCompleted\033[0m]" in view_tasks_output


def test_complete_task():
    tasks.clear()  # Limpar a lista de tarefas no início do teste
    tasks.append({"name": "Task 1", "description": "Description for Task 1", "due_date": "2023-07-15", "completed": False})
    tasks.append({"name": "Task 2", "description": "Description for Task 2", "due_date": "2023-07-16", "completed": False})

    with patch('builtins.input', return_value="2"):
        complete_task()

    assert tasks[1]["completed"] is True


def test_complete_task_invalid_input(capsys):
    tasks.clear()  # Limpar a lista de tarefas no início do teste
    tasks.append({"name": "Task 1", "description": "Description for Task 1", "due_date": "2023-07-15", "completed": False})

    with patch('builtins.input', side_effect=['0', '']):
        with pytest.raises(ValueError):
            complete_task()

    assert tasks[0]["completed"] is False

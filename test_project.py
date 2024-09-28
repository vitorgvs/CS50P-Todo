# test_project.py
import pytest

def test_add_task():
    todo_list = []
    add_task(todo_list)
    assert len(todo_list) == 1

def test_remove_task():
    todo_list = [{"task": "Task 1", "completed": False}]
    remove_task(todo_list)
    assert len(todo_list) == 0

def test_mark_task_as_completed():
    todo_list = [{"task": "Task 1", "completed": False}]
    mark_task_as_completed(todo_list)
    assert todo_list[0]["completed"] == True

def test_display_todo_list():
    todo_list = [{"task": "Task 1", "completed": False}, {"task": "Task 2", "completed": True}]
    display_todo_list(todo_list)
    # This test is more complex and would require mocking user input/output

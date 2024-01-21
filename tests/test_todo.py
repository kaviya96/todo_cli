import pytest
from todo.todo import ToDo

@pytest.fixture
def todo_instance():
    return ToDo()  

#test to check if the returned value for the method listToDo with option even 
def test_list_todo_even(todo_instance, capsys):
    todo_instance.listToDo(2, False, "even")
    captured = capsys.readouterr()
    assert "Title:" in captured.out
    assert "Completed:" in captured.out
    assert "quis ut nam facilis et officia qui" in captured.out
    assert "False" in captured.out


#test to check if the returned value for the method listToDo with option as odd
def test_list_todo_odd(todo_instance, capsys):
    todo_instance.listToDo(10, False, "odd")
    captured = capsys.readouterr()
    assert "illo expedita consequatur quia in" in captured.out
    assert "False" in captured.out


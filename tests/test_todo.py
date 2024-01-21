import pytest
from todo.todo import ToDo

@pytest.fixture
def todo_instance():
    return ToDo()  

def test_list_todo(todo_instance, capsys):
    todo_instance.listToDo(2, False)
    captured = capsys.readouterr()
    assert "Title:" in captured.out
    assert "Completed:" in captured.out
    assert "quis ut nam facilis et officia qui" in captured.out
    assert "False" in captured.out

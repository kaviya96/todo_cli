import pytest
from todo.todo import ToDo
from unittest.mock import patch

@pytest.fixture
def todo_instance():
    return ToDo()  
    
 #test to check the method fetchToDo for a successful request   
@patch('requests.get')
def test_fetchToDo_success(mock_get, todo_instance):
    # Set up the mock response for a successful request
    mock_response = {'userId': 1, 'id': 1, 'title': 'Test Todo', 'completed': False}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response
    result = todo_instance.fetchToDo(1)
    assert result == mock_response

#test to check if the returned value for the method listToDo with option even 
def test_listtToDo_even(todo_instance, capsys):
    todo_instance.listToDo(2, False, "even")
    captured = capsys.readouterr()
    assert "Title:" in captured.out
    assert "Completed:" in captured.out
    assert "quis ut nam facilis et officia qui" in captured.out
    assert "False" in captured.out


#test to check if the returned value for the method listToDo with option as odd
def test_listToDo_odd(todo_instance, capsys):
    todo_instance.listToDo(10, False, "odd")
    captured = capsys.readouterr()
    assert "illo expedita consequatur quia in" in captured.out
    assert "False" in captured.out


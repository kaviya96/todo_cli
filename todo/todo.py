import argparse
import requests


class ToDo:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com/todos/{}"
        self.name = 'ToDo CLI application'

    def fetchToDo(self, index):
        """
        Fetch the TODO item at the specified index from the API.

        Parameters:
        - index (int): The index of the TODO item to fetch.

        Returns:
        dict or None: A dictionary representing the TODO item if the request is successful,
                    otherwise returns None in case of an error.

        Note:
        The returned dictionary has the following structure:
        {
            "userId": int,
            "id": int,
            "title": str,
            "completed": bool
        }
        """
        url = self.base_url.format(index)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error fetching TODO at index {}: {}".format(index, response.status_code))
            return None

    def listToDo(self, value, show_pending):
        """
        List TODO items up to the specified value.

        Parameters:
        - value (int): The upper limit for the TODO indices.
        - show_pending (bool): If True, show pending TODOs; if False, show all TODOs.

        Returns:
        None
        """
        if value < 2:
            raise ValueError("Invalid input: Value must be 2 or greater.")
            
        for i in range(2, value+1, 2):
            todos = self.fetchToDo(i)
            if todos:
                if not isinstance(todos, list):
                    todos = [todos]  # Convert single dictionary to a list
                if show_pending:
                    todos = [todo for todo in todos if not todo['completed']] #gives the todos thats not yet completed
                for todo in todos:
                    print("Title: {}, Completed: {}".format(todo['title'], todo['completed']))
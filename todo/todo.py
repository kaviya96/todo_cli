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

    def listToDo(self, number, show_pending, option):
        """
        List TODO items up to the specified value.

        Parameters:
        - number (int): The number of TODO indices.
        - show_pending (bool): If True, show pending TODOs; if False, show all TODOs.
        - option (string): The IDs of todo should be even or odd or all

        Returns:
        None
        """
            
        for i in range(2 if option == 'even' else 1, number + 1, 1 if option == 'all' else 2): #the range starts at ID 2 if the option is even or 1 for odd or all
            todos = self.fetchToDo(i)
            if todos:
                if not isinstance(todos, list):
                    todos = [todos]  # Convert single dictionary to a list
                if show_pending:
                    todos = [todo for todo in todos if not todo['completed']] #gives the todos thats not yet completed
                for todo in todos:
                    #print("ID:{}, Title: {}, Completed: {}".format(todo['id'], todo['title'], todo['completed']))
                    print("Title: {}, Completed: {}".format(todo['title'], todo['completed']))
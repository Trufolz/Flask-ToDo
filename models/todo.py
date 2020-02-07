from models.data_manager import *


class Todo:
    """ Class representing todo item."""
    todo_objects = []

    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status
        self.todo_objects.append(self)

    def add(self):
        """ Saves/updates todo item in database """
        add_query(self.name, self.status)

    def edit(self):
        """ Saves/updates todo item in database """
        edit_query(self.id, self.name, self.status)

    def toggle(self):
        """ Toggles item's state """
        if self.status == 0:
            self.status = 1
        elif self.status == 1:
            self.status = 0
        toggle_query(self.id, self.status)

    @classmethod
    def get_all(cls):
        """ Retrieves all Todos form database and returns them as list.
        Returns:
            list(Todo): list of all todos
        """
        cls.todo_objects = []
        all_todos = select_all_query()
        for todo in all_todos:
            Todo(todo[0], todo[1], todo[2])

        return cls.todo_objects

    @staticmethod
    def get_by_id(id):
        """ Retrieves todo item with given id from database.
        Args:
            id(int): item id
        Returns:
            Todo: Todo object with a given id
        """
        chosen_todo = select_by_id_query(id)
        chosen_todo_obj = Todo(chosen_todo[0][0], chosen_todo[0][1], chosen_todo[0][2])

        return chosen_todo_obj



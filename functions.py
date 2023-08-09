FILEPATH = 'todos.txt'


def get_todos(path=FILEPATH) -> list:
    """" Get data from file and return the list"""
    with open(path, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, path=FILEPATH):
    """ Write data-list to file"""
    with open(path, 'w') as file:
        file.writelines(todos_arg)

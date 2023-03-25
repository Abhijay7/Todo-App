def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file_loc:
        todos_loc = file_loc.readlines()
    return todos_loc


def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)



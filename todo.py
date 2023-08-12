from colorama import Fore


exit = False

todo_items = []

def get_argument(command):
    command_name, argument = command.split(" ", maxsplit=1)
    return argument

def handle_add_command(command):
    task = get_argument(command)
    print(f"Adding task: {task}")
    todo_items.append(task)

def handle_delete_command(command):
    item_number = get_argument(command)
    print(f"Deleting task: {item_number}")
    todo_items.pop(int(item_number) - 1)

def handle_list_command():
    index = 0
    for todo_item in todo_items:
        index += 1
        print(f"{Fore.BLUE}{index}.{Fore.RESET} {todo_item}")

def handle_open_command(command):
    # Read a list of todo items from a file, one per line
    filename = get_argument(command)
    filename += ".todo.txt"
    with open(filename, "r") as file:
        for line in file:
            todo_items.append(line.strip())

def handle_save_command(command):
    # Save the list to a file, one item per line
    filename = get_argument(command)
    filename += ".todo.txt"
    with open(filename, "w") as file:
        for todo_item in todo_items:
            file.write(f"{todo_item}\n")

def process_command(command):
    if command.startswith("exit"):
        return True
    elif command.startswith("add"):
        handle_add_command(command)
    elif command.startswith("delete"):
        handle_delete_command(command)
    elif command.startswith("list"):
        handle_list_command()
    elif command.startswith("open"):
        handle_open_command(command)
    elif command.startswith("save"):
        handle_save_command(command)
    else:
        print("Command not recognized")
    return False
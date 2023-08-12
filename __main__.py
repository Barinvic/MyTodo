from todo.todo import process_command
from colorama import init, Fore

init()

exit = False
while not exit:
    command = input("Enter command: ")
    exit = process_command(command)
# just comment checking github options

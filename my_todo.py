#import colorama
from colorama import init
init(autoreset=True)
from colorama import Fore

exit=False

user_id=input('Enter your name: ') #getting user
if len(user_id)==0:
    print(Fore.RED+'You did not enter your name. Default file will be used')
    user_id='default_user'
print('Hello,', user_id)

try:                    #creating file for current user; checking if the file already exist (user already registered)
    filename=user_id
    filename+='.todo.txt'
    open(filename,'x')
except FileExistsError:
    print(user_id,'file is ready!')



todo_items=[]  #creating todo list, our workspace
with open(filename, "r") as file:
    for line in file:
        todo_items.append(line.strip())


    def get_argument(command): #define the argument which is an item
        try:
            command_name, argument=command.split(' ', maxsplit=1)
            return argument
        except ValueError:
            print(Fore.RED+'Input error')

while not exit:
    command=input(Fore.LIGHTMAGENTA_EX+'Enter command:'+Fore.RESET)

    if command.startswith('exit'):  #handling soft exit
        with open(filename, "w") as file:
            for todo_item in todo_items:
                file.write(f"{todo_item}\n")
        print(Fore.CYAN+"See you later,",user_id,"!")
        exit=True
    elif command.startswith('add'): #add new entry to current list
        try:
            argument=get_argument(command)
            print(Fore.LIGHTGREEN_EX+f'Adding task: {argument}')
            todo_items.append(argument)
        except TypeError:
            print(Fore.RED+'An argument required - type Help for help')
    elif command.startswith('delete'): #delete existing entry from the current list
        try:
            argument=get_argument(command)
            print(f'Deleting task: {argument}')
            todo_items.pop(int(argument) - 1)
        except TypeError:
            print(Fore.RED+'the string number is required')
        except IndexError:
            print(Fore.RED+'the string number should be in a range')

    elif command.startswith('list'): #print current list
        print(Fore.RED+'Printing...')
        string_number=0
        for todo_item in todo_items:
            string_number+=1
            print(Fore.LIGHTBLUE_EX+f'{string_number}. {todo_item}')
    elif command.startswith('help'):
        print('TODO application using file Yourname.todo.txt to keep your data')
        print('List of commands (case sensitive):')
        print('add - adding new task to list, format: add mytask')
        print('list - print list of recorded tasks, no argument required')
        print('delete - deleting specified string; format: delete 3')
        print('exit - saving your changes and exit from TODO. If You exit with CTRL+C - your changes will not saved')

    else:
        print('Enter valid command (exit, add, delete, list, open)')


from error_class import ErrorClass
from command import Add_Command
from command import Search_Command
from command import Delete_Command
from command import Quit_Command
from command import Help_Command

def verify(command):
    arguments = command.split()

    # checks if command is of form command -option user/platform
    if len(arguments) == 1:
        command = arguments[0]
        if command == 'quit':
            return Quit_Command()
        elif command == 'help':
            return Help_Command()
        else :
            print 'ERROR: invalid command'

    elif len(arguments) == 2:
        command = arguments[0]
        platform = arguments[1]

        # checks if valid command
        if (command == 'search'):
            return Search_Command(platform.lower())

        elif (command == 'delete'):
            return Delete_Command(platform.lower())

        else :
            print 'ERROR: invalid command'
            return None

    elif len(arguments) == 4:
        command = arguments[0]
        platform = arguments[1]
        username = arguments[2]
        password = arguments[3]

        # checks if valid command
        if (command == 'add'):
            return Add_Command(platform.lower(), username, password)

        else :
            print 'ERROR: invalid command'
            return None

    else :
        print 'ERROR: command not found'
        return None

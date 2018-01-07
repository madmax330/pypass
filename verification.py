from error_class import ErrorClass
from password import Password
from command import AddCommand
from command import SearchCommand
from command import DeleteCommand
from command import UpdateCommand
from command import QuitCommand
from command import HelpCommand


COMMANDS = [
    'add',
    'search',
    'update',
    'quit',
    'help',
]


class Verification(ErrorClass):

    def __init__(self):
        super(Verification, self).__init__()
        self.className = 'Verification'

    def verify(self, command):
        # check if first arg is a command
        # call appropriate method for each command
        # return the command
        arguments = command.split()

        # checks if command is of form command -option user/platform
        if len(arguments) == 1:
            command = arguments[0]
            if command == 'quit':
                return QuitCommand()
            elif command == 'help':
                return HelpCommand()
            elif command == 'add':
                return AddCommand(Password('', '', ''))
            elif command == 'update':
                return UpdateCommand(Password('', '', ''))
            else:
                self.add_error('Invalid command.')

        elif len(arguments) == 2:
            command = arguments[0]
            platform = arguments[1]

            # checks if valid command
            if command == 'search':
                return SearchCommand(platform.lower())

            elif command == 'delete':
                return DeleteCommand(platform.lower())

            else:
                self.add_error('Invalid command.')
                return None

        elif len(arguments) == 3:
            command = arguments[0]
            platform = arguments[1]
            password = arguments[2]

        elif len(arguments) == 4:
            command = arguments[0]
            platform = arguments[1]
            username = arguments[2]
            password = arguments[3]

            # checks if valid command
            if command == 'add':
                return AddCommand(Password(platform.lower(), username, password))

            elif command == 'update':
                return UpdateCommand(Password(platform.lower(), username, password))

            else:
                self.add_error('Invalid command.')
                return None

        elif len(arguments) == 5:
            command = arguments[0]
            platform = arguments[1]
            username = arguments[2]
            password = arguments[3]
            flag = arguments[4]

            if command == 'update':
                return UpdateCommand(Password(platform.lower(), username, password), flag=flag)
            else:
                self.add_error('Invalid command.')
                return None

        else:
            self.add_error('Command not found.')
            return None

    def get_add_command(self, args):
        pass

    def get_search_command(self, args):
        pass

    def get_update_command(self, args):
        pass

    def get_quit_command(self, args):
        pass

    def get_help_command(self, args):
        pass

    def __get_command(self, command):  # returns a string value of the command
        try:
            return COMMANDS[COMMANDS.index(command)]
        except ValueError:
            return ''


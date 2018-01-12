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

        if len(arguments) > 0:
            command = arguments[0]
            if command == 'quit':
                return self.get_quit_command(arguments)
            elif command == 'help':
                return self.get_help_command(arguments)
            elif command == 'add':
                return self.get_add_command(arguments)
            elif command == 'search':
                return self.get_search_command(arguments)
            elif command == 'delete':
                return self.get_delete_command(arguments)
            elif command == 'update':
                return self.get_update_command(arguments)
            else:
                self.add_error('Command not found.')
                return None


    def get_add_command(self, args):
        if len(args) == 1:
            return AddCommand(Password('', '', ''))
        elif len(args) == 4:
            platform = args[1]
            username = args[2]
            password = args[3]
            return AddCommand(Password(platform.lower(), username, password))
        else:
            self.add_error('Invalid command.')
            return None

    def get_search_command(self, args):
        if len(args) == 2:
            platform = args[1]
            return SearchCommand(platform.lower())
        else:
            self.add_error('Invalid command.')
            return None

    def get_delete_command(self, args):
        if len(args) == 2:
            platform = args[1]
            return DeleteCommand(platform.lower())
        else:
            self.add_error('Invalid command.')
            return None

    def get_update_command(self, args):
        if len(args) == 1:
            return UpdateCommand(Password('', '', ''))
        elif len(args) == 4:
            platform = args[1]
            username = args[2]
            password = args[3]
            return UpdateCommand(Password(platform.lower(), username, password))
        elif len(args) == 5:
            platform = args[1]
            username = args[2]
            password = args[3]
            flag = args[4]
            return UpdateCommand(Password(platform.lower(), username, password), flag=flag)
        else:
            self.add_error('Invalid command.')
            return None

    def get_quit_command(self, args):
        if len(args) == 1:
            return QuitCommand()
        else:
            self.add_error('Invalid command.')
            return None

    def get_help_command(self, args):
        if len(args) == 1:
            return HelpCommand()
        else:
            self.add_error('Invalid command.')
            return None

    # def __get_command(self, command):  # returns a string value of the command
        # try:
            # return COMMANDS[COMMANDS.index(command)]
        # except ValueError:
            # return ''

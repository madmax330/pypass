from error_class import ErrorClass
from password import Password
from database import Database
from encryption import  Encryption


class Command(ErrorClass):  # Base Command Class

    def __init__(self):
        super(ErrorClass, self).__init__()
        self.className = 'Command'

    def run(self):
        print('Run method not implemented.')


class NewCommand(Command):  # New password command

    def __init__(self):
        super(Command, self).__init__()

    def run(self):
        pass


class SearchCommand(Command):  # Search password command

    def __init__(self):
        super(Command, self).__init__()

    def run(self):
        pass


class DeleteCommand(Command):  # Delete password command

    def __init__(self):
        super(Command, self).__init__()

    def run(self):
        pass



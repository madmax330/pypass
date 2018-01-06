from error_class import ErrorClass
from password import Password
from encryption import  Encryption

class Add_Command:
    def __init__ (self, platform, username, password):
        self.command = 'add'
        self.platform = platform
        self.username = username
        self.password = password

    def __repr__ (self):
        return "%s: %s" % (self.command, self.platform)

class Search_Command:
    def __init__ (self, platform):
        self.command = 'search'
        self.platform = platform

    def __repr__ (self):
        return "%s: %s" % (self.command, self.platform)

class Delete_Command:
    def __init__ (self, platform):
        self.command = 'delete'
        self.platform = platform

    def __repr__ (self):
            return "%s: %s" % (self.command, self.platform)

class Quit_Command:
    def __init__ (self):
        self.command = 'quit'
        self.platform = None

    def __repr__ (self):
        return "%s: %s" % (self.command, self.platform)

class Help_Command:
    def __init__ (self):
        self.command = 'help'
        self.platform = None

    def __repr__ (self):
        return "%s: %s" % (self.command, self.platform)

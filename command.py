

class QuitException(Exception):
    pass


class Command:

    def __init__(self):
        self.className = 'Command'

    def run(self, db):
        print('Run method was not implemented.')


class AddCommand(Command):

    def __init__(self, password):
        super(AddCommand, self).__init__()
        self.command = 'add'
        self.password = password

    def __repr__(self):
        return "%s: %s" % (self.command, self.password.platform)

    def run(self, db):
        db.add_password(self.password)
        print('Password added successfully.')


class SearchCommand(Command):

    def __init__(self, platform):
        super(SearchCommand, self).__init__()
        self.command = 'search'
        self.platform = platform

    def __repr__(self):
        return "%s: %s" % (self.command, self.platform)

    def run(self, db):
        results = db.search_password(self.platform)
        if results:
            for x in results:
                print(str(x))
        else:
            print('No password entry found.')


class DeleteCommand(Command):

    def __init__(self, platform):
        super(DeleteCommand, self).__init__()
        self.command = 'delete'
        self.platform = platform

    def __repr__(self):
            return "%s: %s" % (self.command, self.platform)

    def run(self, db):
        results = db.search_password(self.platform)
        if results:
            db.delete_password(self.platform)
            print('Password deleted successfully.')
        else:
            print('No password entry found.')


class QuitCommand(Command):

    def __init__(self):
        super(QuitCommand, self).__init__()
        self.command = 'quit'

    def __repr__(self):
        return "%s" % self.command

    def run(self, db):
        raise QuitException('Quit command entered.')


class HelpCommand(Command):

    def __init__(self):
        super(HelpCommand, self).__init__()
        self.command = 'help'

    def __repr__(self):
        return "%s" % self.command

    def run(self, db):
        print('Commands:')
        print('Add:\n add <platform> <username> <password>')
        print('Search:\n search <platform>')
        print('Delete:\n delete <platform>')
        print('Quit: quit')

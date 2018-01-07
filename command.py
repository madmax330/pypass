from error_class import BColors


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
        if self.password.is_blank():
            self.password.platform = input('Platform:')
            self.password.username = input('Username:')
            self.password.password = input('Password:')
        if not self.password.is_blank():
            db.add_password(self.password)
            print(BColors.OKGREEN + 'Password added successfully.' + BColors.ENDC)
        else:
            print(BColors.FAIL + 'Platform, Username and Password cannot be left blank.' + BColors.ENDC)


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
                print(BColors.OKBLUE + str(x))
            print(BColors.ENDC)
        else:
            print(BColors.WARNING + 'No password entry found.' + BColors.ENDC)


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
            print(BColors.OKGREEN + 'Password deleted successfully.' + BColors.ENDC)
        else:
            print(BColors.WARNING + 'No password entry found.' + BColors.ENDC)


class UpdateCommand(Command):

    def __init__(self, password):
        super(UpdateCommand, self).__init__()
        self.command = 'update'
        self.password = password

    def __repr__(self):
        return "%s: %s" % (self.command, self.password.platform)

    def run(self, db):
        if self.password.is_blank():
            self.password.platform = input('Platform:')
            self.password.username = input('Username:')
            self.password.password = input('Password:')
        if not self.password.is_blank():
            results = db.search_password(self.password.platform)
            if results:
                db.update_password(self.password)
                print(BColors.OKGREEN + 'Password updated successfully.' + BColors.ENDC)
            else:
                print(BColors.WARNING + 'No password entry found.' + BColors.ENDC)
        else:
            print(BColors.FAIL + 'Platform, Username and Password cannot be left blank.' + BColors.ENDC)


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
        print('Update:\n update <platform> <username> <password>')
        print('Quit: quit')

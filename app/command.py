from app.error_class import ErrorClass
from app.ui.colors import BColors


class QuitException(Exception):
    pass


class Command(ErrorClass):

    def __init__(self):
        super(Command, self).__init__()
        self.className = 'Command'
        self.command = ''
        self.status = False

    def run(self, db):
        print('Run method was not implemented.')

    def get_result(self):
        return self.status

    def check_conditions(self):
        print('Check conditions not implemented.')

    def print_success(self):
        print('Print success not implemented.')


class AddCommand(Command):

    def __init__(self, password):
        super(AddCommand, self).__init__()
        self.command = 'add'
        self.password = password

    def __repr__(self):
        return "%s: %s" % (self.command, self.password.platform)

    def run(self, db):
        if self.password.is_blank():
            self.__step_by_step()
        if self.check_conditions():
            db.add_password(self.password)
            self.status = True
            print(BColors.OKGREEN + 'Password added successfully.' + BColors.ENDC)

        self.print_errors()

    def __step_by_step(self):
        self.password.platform = input('Platform:').lower()
        self.password.username = input('Username:')
        self.password.password = input('Password:')

    def check_conditions(self):
        if self.password.is_blank():
            self.add_error('Platform, Username and Password cannot be left blank.')
            return False
        return True


class SearchCommand(Command):

    def __init__(self, platform):
        super(SearchCommand, self).__init__()
        self.command = 'search'
        self.platform = platform
        self.results = []

    def __repr__(self):
        return "%s: %s" % (self.command, self.platform)

    def run(self, db):
        self.results = db.search_password(self.platform)
        if self.results:
            self.status = True
            for x in self.results:
                print(BColors.OKBLUE + str(x))
            print(BColors.ENDC)
        else:
            print(BColors.WARNING + 'No password entry found.' + BColors.ENDC)

    def get_result(self):
        return self.results


class DeleteCommand(Command):

    def __init__(self, platform, username):
        super(DeleteCommand, self).__init__()
        self.command = 'delete'
        self.platform = platform
        self.username = username

    def __repr__(self):
            return "%s: %s %s" % (self.command, self.platform, self.username)

    def run(self, db):
        results = db.search_password(self.platform, username=self.username)
        if results:
            db.delete_password(self.platform, self.username)
            self.print_success()
            self.status = True
        else:
            print(BColors.WARNING + 'No password entry found.' + BColors.ENDC)

    def print_success(self):
        print(BColors.OKGREEN + 'Password deleted successfully.' + BColors.ENDC)


class UpdateCommand(Command):

    def __init__(self, password, flag='', new_username=None):
        super(UpdateCommand, self).__init__()
        self.command = 'update'
        self.password = password
        self.flag = flag
        self.new_username = new_username if new_username else ''

    def __repr__(self):
        return "%s: %s" % (self.command, self.password.platform)

    def run(self, db):
        if self.password.is_blank():
            self.__step_by_step()
        if self.flag == '-u':
            self.__get_new_username()
        if self.check_conditions():
            results = db.search_password(self.password.platform, username=self.password.username)
            if results:
                db.update_password(self.password, self.new_username)
                self.print_success()
                self.status = True
                print('Old Password(s):')
                print_passwords(results)
                results = db.search_password(self.password.platform)
                print('New Password(s):')
                print_passwords(results)
            else:
                print(BColors.WARNING + 'No password entry found.' + BColors.ENDC)

        self.print_errors()

    def check_conditions(self):
        no_error = True
        if self.password.is_blank():
            self.add_error('Platform, Username and Password cannot be left blank.')
            no_error = False
        if self.flag == '-u' and not self.new_username:
            self.add_error('New username cannot be left blank.')
        return no_error

    def print_success(self):
        print(BColors.OKGREEN + 'Password updated successfully.' + BColors.ENDC)

    def __step_by_step(self):
        self.password.platform = input('Platform: ')
        self.password.username = input('Username: ')
        self.password.password = input('Password: ')
        change_username = input('Change username? (Y)es/(N)o: ')
        if change_username and change_username.lower() == 'y':
            self.flag = '-u'

    def __get_new_username(self):
        self.new_username = input('New Username: ')


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
        print('Update:\n update <platform> <username> <password> <-u>')
        print('Quit: quit')


def print_passwords(l):
    for x in l:
        print(str(x))
    print(BColors.ENDC)

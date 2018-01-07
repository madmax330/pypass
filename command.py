from error_class import BColors, ErrorClass


class QuitException(Exception):
    pass


class Command(ErrorClass):

    def __init__(self):
        super(Command, self).__init__()
        self.className = 'Command'

    def run(self, db):
        print('Run method was not implemented.')

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
            print(BColors.OKGREEN + 'Password added successfully.' + BColors.ENDC)

        self.print_errors()

    def __step_by_step(self):
        self.password.platform = input('Platform:')
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
            self.print_success()
        else:
            print(BColors.WARNING + 'No password entry found.' + BColors.ENDC)

    def print_success(self):
        print(BColors.OKGREEN + 'Password deleted successfully.' + BColors.ENDC)


class UpdateCommand(Command):

    def __init__(self, password, flag=''):
        super(UpdateCommand, self).__init__()
        self.command = 'update'
        self.password = password
        self.flag = flag
        self.new_username = ''

    def __repr__(self):
        return "%s: %s" % (self.command, self.password.platform)

    def run(self, db):
        if self.password.is_blank():
            self.__step_by_step()
        if self.flag == '-u':
            self.__get_new_username()
        if self.check_conditions():
            results = db.search_password(self.password.platform)
            if results:
                db.update_password(self.password, self.new_username)
                self.print_success()
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
        print('Update:\n update <platform> <username> <password>')
        print('Quit: quit')


def print_passwords(l):
    for x in l:
        print(str(x))
    print(BColors.ENDC)

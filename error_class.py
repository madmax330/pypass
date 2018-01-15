
class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ErrorClass:

    def __init__(self):
        self.className = 'Error Class'
        self.errors = []

    def add_error(self, error):
        self.errors.append(error)

    def print_errors(self):
        if len(self.errors):
            print(BColors.FAIL + self.className + ' Errors:')
            for x in self.errors:
                print(' - ' + x)
                print(BColors.ENDC)





from app.ui.colors import BColors


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





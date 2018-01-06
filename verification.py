from error_class import ErrorClass


class Verification(ErrorClass):

    def __init__(self):
        super(ErrorClass, self).__init__()
        self.className = 'Verification'

    def verify_command(self, command):
        pass

    def verify_flag(self, flag):
        pass

    def verify_value(self, val):
        pass

    def is_empty(self, val):
        if val:
            return False
        return True








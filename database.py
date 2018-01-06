from error_class import ErrorClass


class Database(ErrorClass):

    def __init__(self):
        super(ErrorClass, self).__init__()
        self.className = 'Database'

    def store_password(self, password):
        pass

    def search_password(self, flag, val):
        pass

    def delete_password(self, flag, val):
        pass

    def load_passwords(self):
        pass



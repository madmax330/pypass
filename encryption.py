from error_class import ErrorClass


class EncryptionClass(ErrorClass):

    def __init__(self):
        super(ErrorClass, self).__init__()
        self.className = 'Encryption'

    def encrypt(self, val):
        pass

    def decrypt(self, val):
        pass





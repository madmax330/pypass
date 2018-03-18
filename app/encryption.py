from cryptography.fernet import Fernet
from configparser import ConfigParser


class Encryption:

    def __init__(self):
        config = ConfigParser()
        config.read('pypass.conf')
        self.__key = self.__sanitize_key(config['DEFAULT']['secret_key'])

    def encrypt_password(self, password):
        password.password = self.__encrypt(password.password.encode('utf-8')).decode('utf-8')
        return password

    def decrypt_password(self, password):
        password.password = self.__decrypt(password.password.encode('utf-8')).decode('utf-8')
        return password

    def encrypt_string(self, val):
        return self.__encrypt(val.encode('utf-8')).decode('utf-8')

    def __encrypt(self, val):
        f = Fernet(self.__key)
        return f.encrypt(val)

    def __decrypt(self, val):
        f = Fernet(self.__key)
        return f.decrypt(val)

    def __sanitize_key(self, key):
        key = key[2:46]
        return key.encode('utf-8')



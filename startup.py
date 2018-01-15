from configparser import ConfigParser


class StartupException(Exception):
    pass


def startup():
    conf = ConfigParser()
    if not conf.read('pypass.conf'):
        raise StartupException('Configuration file cannot be found.')
    if not conf['DEFAULT']:
        raise StartupException('Pypass secret key not found.')







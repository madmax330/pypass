from configparser import ConfigParser
from cryptography.fernet import Fernet
import sqlite3


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print('Writing config...')
config = ConfigParser()
key = Fernet.generate_key()
config['DEFAULT'] = {
    'secret_key': key
}

with open('pypass.conf', 'w') as config_file:
    config.write(config_file)

print(BColors.OKGREEN + ' Config successful.' + BColors.ENDC)
print('Creating database...')
try:
    db = sqlite3.connect('db.sqlite3')
    cur = db.cursor()
    cur.execute('DROP TABLE password;')
    cur.execute(
        'CREATE TABLE password(platform varchar(256) not null, username varchar(256) not null, password varchar(256) not null);'
    )
    print(BColors.OKGREEN + 'Database created successfully.' + BColors.ENDC)
except sqlite3.Error as e:
    print(BColors.FAIL + 'Could not connect to the database: ' + str(e) + BColors.ENDC)



from configparser import ConfigParser
from cryptography.fernet import Fernet
from app.ui.colors import BColors
import sqlite3

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



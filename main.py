#!/usr/bin/env python3

from verification import Verification
from command import QuitException
from sqlite3 import Error
from database import Database


def main():
    try:
        db = Database()
        while True:
            verify = Verification()
            var = input("Please enter a command: ")
            command = verify.verify(var)
            if command:
                command.run(db)
            else:
                verify.print_errors()

    except (QuitException, Error) as e:
        if isinstance(e, QuitException):
            print('Thanks for using pypass, until next time!')
        else:
            print(str(e))
            print('Error connecting to the database, please relaunch the application.')


if __name__ == 'main':
    main()


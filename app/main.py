import sys

from app.startup import startup, StartupException
from app.database import Database
from app.verification import Verification
from app.command import QuitException
from sqlite3 import Error


from app.ui.main import PypassWindow
import tkinter as tk


def main():

    if len(sys.argv) > 1:
        if sys.argv[1] == 'bash':
            try:
                startup()
            except StartupException as e:
                print('Error starting up pypass.\n' + str(e))
                return

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
        else:
            print('Unknown command.')
    else:
        root = tk.Tk()
        pypass = PypassWindow(root)
        pypass.pack(fill=tk.BOTH, expand=True)
        root.mainloop()







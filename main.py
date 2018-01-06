import database
from password import Password
from verification import verify
from command import Quit_Command
from command import Help_Command

def main():
    while True:
        var = raw_input("Please enter a command: ")
        command = verify(var)
        # print command
        if (not command):
            pass
        elif isinstance(command, Quit_Command):
            break
        elif isinstance(command, Help_Command):
            print 'Commands:'
            print 'Add:\n add <platform> <username> <password>'
            print 'Search:\n search <platform>'
            print 'Delete:\n delete <platform>'
            print 'Quit: quit'
        else :
            print database.execute(command)

        # Database.toString()

if __name__ == '__main__':
    main()

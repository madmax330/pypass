from error_class import ErrorClass

from command import Add_Command
from command import Search_Command
from command import Delete_Command
from password import Password
from password import Platform
from password import Username

passwords = []

def execute(command):
    if isinstance(command, Add_Command):
        return add_password(command)
    elif isinstance(command, Search_Command):
        return search_password(command)
    elif isinstance(command, Delete_Command):
        return delete_password(command)
    else:
        print 'ERROR: could not execute command'
        return False

def add_password(command):
    platform_str = command.platform
    username_str = command.username
    password_str = command.password

    platform = Platform(platform_str)
    username = Username(username_str)

    password = Password(platform, username, password_str)
    passwords.append(password)
    return 'Successfully Added: %s' % password

def search_password(command):
    platform = command.platform
    match = []
    for p in passwords:
        if(p.platform.name == platform):
            match.append(p)
    if match.__len__() == 0:
        return 'Not Found'
    else:
        return 'Results: %s' % match

def delete_password(command):
    platform = command.platform
    for p in passwords:
        if(p.platform.name == platform):
            passwords.remove(p)
            return 'Successfully Deleted: %s' % p
    return 'Not Found'

def toString():
    for p in passwords:
        print p

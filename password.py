
class Username:
    def __init__ (self, name):
        self.name = name

    def rename (self, new_name):
        self.name = new_name

    def __repr__ (self):
        return self.name

class Platform:
    def __init__ (self, name):
        self.name = name

    def rename (self, new_name):
        self.name = new_name

    def __repr__ (self):
        return self.name

class Password:
    def __init__(self, platform, username, password):
        self.platform = platform
        self.username = username
        self.password = password

    def reset(self, new_pass):
        pass

    def __repr__ (self):
        return "\n%s \nUsername: %s \nPassword: %s" % (self.platform, self.username, self.password)

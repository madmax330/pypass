

class Password:

    def __init__(self, platform, username, password):
        self.platform = platform
        self.username = username
        self.password = password

    def reset(self, new_pass):
        self.password = new_pass

    def is_blank(self):
        return self.platform and self.username and self.password

    def __repr__(self):
        return "%s \nUsername: %s \nPassword: %s" % (self.platform, self.username, self.password)

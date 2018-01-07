from password import Password
import sqlite3
import html


class Database:

    def __init__(self):
        self.db = sqlite3.connect('db.sqlite3')

    def add_password(self, password):
        cur = self.db.cursor()
        cur.execute("INSERT INTO password values(?, ?, ?)", (
            html.escape(password.platform),
            html.escape(password.username),
            html.escape(password.password)
        ))
        self.db.commit()

    def search_password(self, platform):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM password WHERE platform=?", (platform,))
        l = cur.fetchall()
        results = []
        for x in l:
            results.append(Password(x[0], x[1], x[2]))
        return results

    def delete_password(self, platform):
        cur = self.db.cursor()
        cur.execute("DELETE FROM password WHERE platform=?", (platform,))
        self.db.commit()

    def update_password(self, password, new_username):
        cur = self.db.cursor()
        if new_username:
            if password.username:
                cur.execute("UPDATE password SET username=?, password=? WHERE platform=? AND username=?", (
                    new_username,
                    password.password,
                    password.platform,
                    password.username,
                ))
            else:
                cur.execute("UPDATE password SET username=?, password=? WHERE platform=?", (
                    new_username,
                    password.password,
                    password.platform,
                ))
        else:
            if password.username:
                cur.execute("UPDATE password SET password=? WHERE platform=? AND username=?", (
                    password.password,
                    password.platform,
                    password.username,
                ))
            else:
                cur.execute("UPDATE password SET password=? WHERE platform=?", (
                    password.password,
                    password.platform,
                ))
        self.db.commit()

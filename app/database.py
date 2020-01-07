import sqlite3
import html
from app.encryption import Encryption
from app.password import Password


class Database:
    def __init__(self):
        self.db = sqlite3.connect('db.sqlite3')
        self.encryption = Encryption()

    def add_password(self, password):
        password = self.encryption.encrypt_password(password)
        cur = self.db.cursor()
        cur.execute("INSERT INTO password VALUES(?, ?, ?)", (
            html.escape(password.platform),
            html.escape(password.username),
            html.escape(password.password)
        ))
        self.db.commit()

    def search_password(self, platform, username=None):
        cur = self.db.cursor()
        results = []
        if username:
            cur.execute("SELECT * FROM password WHERE platform=? AND username=? COLLATE NOCASE", (platform, username))
            l = cur.fetchall()
            for x in l:
                results.append(self.encryption.decrypt_password(Password(x[0], x[1], x[2])))
            return results
        else:
            cur.execute("SELECT * FROM password WHERE platform=? COLLATE NOCASE", (platform,))
            l = cur.fetchall()
            for x in l:
                results.append(self.encryption.decrypt_password(Password(x[0], x[1], x[2])))
            return results

    def delete_password(self, platform, username):
        cur = self.db.cursor()
        cur.execute("DELETE FROM password WHERE platform=? AND username=?", (platform, username))
        self.db.commit()

    def update_password(self, password, new_username):
        password = self.encryption.encrypt_password(password)
        cur = self.db.cursor()
        if new_username:
            cur.execute("UPDATE password SET username=?, password=? WHERE platform=? AND username=?", (
                new_username,
                password.password,
                password.platform,
                password.username,
            ))
        else:
            cur.execute("UPDATE password SET password=? WHERE platform=? AND username=?", (
                password.password,
                password.platform,
                password.username,
            ))
        self.db.commit()

import tkinter as tk

from app.password import Password
from app.command import AddCommand


class NewPasswordWindow(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.platform_entry = None
        self.username_entry = None
        self.password_entry = None

        self.init_window()

    def init_window(self):

        # First row elements
        label = tk.Label(self, text='New password')
        label.grid(column=0, row=0)

        # Second row elements
        platform_label = tk.Label(self, text='Platform: ')
        platform_label.grid(column=0, row=1)
        self.platform_entry = tk.Entry(self)
        self.platform_entry.grid(column=1, row=1)

        # Third row elements
        username_label = tk.Label(self, text='Username: ')
        username_label.grid(column=0, row=2)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(column=1, row=2)

        # Fourth row elements
        password_label = tk.Label(self, text='Password: ')
        password_label.grid(column=0, row=3)
        self.password_entry = tk.Entry(self)
        self.password_entry.grid(column=1, row=3)

        # Fifth row elements
        cancel_btn = tk.Button(self, text='Cancel', command=self.cancel)
        cancel_btn.grid(column=0, row=4)

        cancel_btn = tk.Button(self, text='Save', command=self.add_password)
        cancel_btn.grid(column=1, row=4)

    def add_password(self):
        password = Password(
            self.platform_entry.get(),
            self.username_entry.get(),
            self.password_entry.get()
        )
        if password.is_blank():
            self.master.show_message('All password fields are required.', error=True)
        else:
            add = AddCommand(password)
            add.run(self.master.db)
            if add.get_result():
                self.master.clear_messages()
                self.master.show_message('Password added successfully')
                self.platform_entry.delete(0, tk.END)
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
            else:
                self.master.show_message('Unable to add password, try again.', error=True)

    def cancel(self):
        self.master.clear_ext_window()





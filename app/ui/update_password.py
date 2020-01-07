import tkinter as tk

from app.password import Password
from app.command import UpdateCommand


class UpdatePasswordWindow(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.password = None

        self.platform_label = None
        self.username_entry = None
        self.password_entry = None

        self.init_window()

    def init_window(self):

        # First row elements
        label = tk.Label(self, text='Update password')
        label.grid(column=0, row=0)

        # Second row elements
        platform_label = tk.Label(self, text='Platform: ')
        platform_label.grid(column=0, row=1)
        self.platform_label = tk.Label(self)
        self.platform_label.grid(column=1, row=1)

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

        cancel_btn = tk.Button(self, text='Save', command=self.update_password)
        cancel_btn.grid(column=1, row=4)

    def update_password(self):
        password = Password(
            self.password.platform,
            self.password.username,
            self.password_entry.get()
        )
        if password.is_blank():
            self.master.show_message('All password fields are required.', error=True)
        else:
            update = UpdateCommand(
                password,
                new_username=self.username_entry.get() if self.username_entry.get() else ''
            )
            update.run(self.master.db)
            if update.get_result():
                self.master.clear_messages()
                self.master.show_message('Password updated successfully.')
            else:
                self.master.show_message('Error updating password, try again.', error=True)

    def cancel(self):
        self.master.clear_ext_window()

    def set_password(self, password):
        self.password = password
        self.platform_label.grid_forget()
        self.platform_label.config(text=password.platform)
        self.platform_label.grid(column=1, row=1)
        self.username_entry.delete(0, tk.END)
        self.username_entry.insert(0, password.username)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password.password)






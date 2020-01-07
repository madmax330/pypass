import tkinter as tk
import pyperclip
from app.command import DeleteCommand


class SearchResultsWindow(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.results = []

        self.label = tk.Label(self)

    def load_results(self, platform, results):
        self.clear_results()

        self.label.grid_forget()
        self.label.config(text=platform + ' search results')
        self.label.grid(column=0, row=0, sticky="w")
        close_btn = tk.Button(self, text='Close search results', command=self.close_search)

        if results:
            row = 1
            for x in results:
                search_result = SearchResult(self, x, row)
                self.results.append(search_result)
                row += 1
            close_btn.grid(column=0, row=row, sticky="w")
        else:
            self.master.show_message('No results found for platform: ' + platform, error=True)

    def clear_results(self):
        self.label.grid_forget()
        for x in self.results:
            x.destroy()
        self.results.clear()

    def close_search(self):
        self.master.clear_ext_window()


class SearchResult:

    def __init__(self, master, password, row):
        self.master = master
        self.password = password
        self.row = row

        self.username_label = None
        self.password_label = None
        self.password_btn = None
        self.copy_btn = None
        self.edit_btn = None
        self.delete_btn = None

        self.init_window()

    def init_window(self):

        self.username_label = tk.Label(self.master, text=self.password.username)
        self.username_label.grid(column=0, row=self.row, sticky="w")

        self.password_btn = tk.Button(self.master, text='Click to view', command=self.view_password)
        self.password_btn.grid(column=1, row=self.row, sticky="w")

        self.password_label = tk.Label(self.master, text=self.password.password)

        self.copy_btn = tk.Button(self.master, text='Copy', command=self.copy_password)
        self.copy_btn.grid(column=2, row=self.row, sticky="w")

        self.edit_btn = tk.Button(self.master, text='Edit', command=self.update_password)
        self.edit_btn.grid(column=3, row=self.row, sticky="w")

        self.delete_btn = tk.Button(self.master, text='x', command=self.delete_password)
        self.delete_btn.grid(column=4, row=self.row, sticky="w")

    def view_password(self):
        self.password_btn.grid_forget()
        self.password_label.grid(column=1, row=self.row, sticky="w")

    def copy_password(self):
        pyperclip.copy(self.password_label.cget('text'))

    def update_password(self):
        self.master.master.load_update_password(self.password)

    def delete_password(self):
        delete = DeleteCommand(self.password.platform, self.password.username)
        delete.run(self.master.master.db)
        if delete.get_result():
            self.master.master.show_message('Password for ' + delete.platform + ' successfully deleted.')
        else:
            self.master.master.show_message('Unable to delete password, try again.', error=True)
        self.master.close_search()

    def get_username_label(self):
        return self.username_label

    def get_password_btn(self):
        return self.password_btn

    def get_password_label(self):
        return self.password_label

    def get_copy_btn(self):
        return self.copy_btn

    def get_edit_btn(self):
        return self.edit_btn

    def get_delete_btn(self):
        return self.delete_btn

    def destroy(self):
        self.username_label.grid_forget()
        self.password_btn.grid_forget()
        self.password_label.grid_forget()
        self.copy_btn.grid_forget()
        self.edit_btn.grid_forget()
        self.delete_btn.grid_forget()





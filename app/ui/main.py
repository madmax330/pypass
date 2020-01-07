import tkinter as tk
from app.ui.settings import SettingsWindow
from app.ui.export import ExportWindow
from app.ui.new_password import NewPasswordWindow
from app.ui.update_password import UpdatePasswordWindow
from app.ui.search_results import SearchResultsWindow

from app.command import SearchCommand
from app.database import Database


class PypassWindow(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.db = Database()

        self.main_windows = {
            'main': MainWindow(self),
            'settings': SettingsWindow(self),
            'export': ExportWindow(self),
        }

        self.ext_windows = {
            'new_password': NewPasswordWindow(self),
            'update_password': UpdatePasswordWindow(self),
            'search_results': SearchResultsWindow(self)
        }

        self.message_label = tk.Label(self)
        self.init_window()

    def init_window(self):
        self.master.title("Pypass")

        main_menu = tk.Menu(self.master)
        self.master.config(menu=main_menu)

        file_menu = tk.Menu(main_menu)
        file_menu.add_command(label='Settings', command=lambda: self.load_main_window('settings'))
        file_menu.add_command(label='Quit', command=self.quit_clicked)

        main_menu.add_cascade(label='File', menu=file_menu)
        self.load_main_window('main')

    def load_main_window(self, window):
        self.clear_messages()
        for key, value in self.main_windows.items():
            value.pack_forget()
        self.main_windows[window].pack(expand=True, fill=tk.BOTH)

    def clear_ext_window(self):
        for key, value in self.ext_windows.items():
            value.pack_forget()

    def load_search_results(self, search, results):
        self.clear_ext_window()
        self.clear_messages()
        self.ext_windows['search_results'].load_results(search, results)
        self.ext_windows['search_results'].pack()

    def load_update_password(self, password):
        self.clear_ext_window()
        self.clear_messages()
        self.ext_windows['update_password'].set_password(password)
        self.ext_windows['update_password'].pack()

    def load_new_password(self):
        self.clear_ext_window()
        self.clear_messages()
        self.ext_windows['new_password'].pack()

    def clear_messages(self):
        self.message_label.pack_forget()

    def show_message(self, msg, error=False):
        self.message_label.config(text=msg)
        self.message_label.pack()

    def quit_clicked(self):
        exit()


class MainWindow(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.search_entry = None

        self.init_window()

    def init_window(self):

        # First row elements
        label = tk.Label(self, text="Search password")
        label.grid(column=0, row=0, sticky="w")

        # Second row elements
        self.search_entry = tk.Entry(self)
        self.search_entry.grid(column=0, row=1)

        search_btn = tk.Button(self, text='Search', command=self.search_password)
        search_btn.grid(column=1, row=1)

        # Third row elements
        new_btn = tk.Button(self, text='New password', command=self.new_password)
        new_btn.grid(column=0, row=2, sticky="w")

    def search_password(self):
        search_string = self.search_entry.get()
        if search_string:
            search = SearchCommand(search_string)
            search.run(self.master.db)
            self.master.load_search_results(search_string, search.get_result())

    def new_password(self):
        self.master.load_new_password()







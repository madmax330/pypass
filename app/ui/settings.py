import tkinter as tk


class SettingsWindow(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master

        self.init_window()

    def init_window(self):

        # First row elements
        label = tk.Label(self, text="Settings")
        label.grid(column=0, row=0)

        # Second row elements
        import_btn = tk.Button(self, text='Import passwords', command=self.import_passwords)
        import_btn.grid(column=0, row=1)

        export_btn = tk.Button(self, text='Export passwords', command=self.export_passwords)
        export_btn.grid(column=1, row=1)

        # Third row elements
        back_btn = tk.Button(self, text='Back', command=self.back)
        back_btn.grid(column=0, row=2)

    def import_passwords(self):
        pass

    def export_passwords(self):
        self.master.load_main_window('export')

    def back(self):
        self.master.load_main_window('main')



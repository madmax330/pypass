import tkinter as tk


class ExportWindow(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.email_entry = None

        self.init_window()

    def init_window(self):

        # First row elements
        label = tk.Label(self, text='Export passwords')
        label.grid(column=0, row=0)

        # Second row elements
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(column=0, row=1)

        # Third row elements
        cancel_btn = tk.Button(self, text='Cancel', command=self.cancel)
        cancel_btn.grid(column=0, row=2)

        export_btn = tk.Button(self, text='Export', command=self.export)
        export_btn.grid(column=1, row=2)

    def cancel(self):
        self.master.load_main_window('main')

    def export(self):
        pass


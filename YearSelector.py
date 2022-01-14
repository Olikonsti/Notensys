from tkinter import *
import tkinter.ttk as ttk
from tkdarktitle import *

class YearSelector(Tk):
    def __init__(self, notensys):
        super().__init__()
        if notensys.dark:
            self.config(bg="#1c1c1c")
        self.notensys = notensys

        if notensys.dark:
            dark_title_bar(self)
            self.tk.call("source", "DATA/theme/sun-valley.tcl")
            self.tk.call("set_theme", "dark")

        self.notensys = notensys
        self.title("Jahr wählen")
        self.geometry("300x100")
        #self.resizable(False, False)

        self.iconbitmap("DATA/icon.ico")

        self.protocol("WM_DELETE_WINDOW", self.clean_exit)

        self.years = self.notensys.save_manager.list_saves()
        self.option_var = StringVar(self)
        self.selector = ttk.OptionMenu(self, self.option_var, self.years[0], *self.years)
        self.selector.pack(side=LEFT, padx=(20,0), pady=20)

        self.apply_btn = ttk.Button(self, text="Weiter", command=self.exit)
        self.apply_btn.pack(side=RIGHT, anchor=SW, padx=(5, 10), pady=(0, 10))

        self.open_folder_btn = ttk.Button(self, text="Ordner öffnen", command=self.notensys.save_manager.open_folder)
        self.open_folder_btn.pack(side=RIGHT, anchor=SW, padx=(10, 0), pady=(0, 10))



        self.mainloop()

    def exit(self):
        self.notensys.splash_screen.destroy()
        self.destroy()

    def clean_exit(self):
        raise SystemExit

    def get_selection(self):
        return self.option_var.get()
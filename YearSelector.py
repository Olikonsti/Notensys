from tkinter import *
import tkinter.ttk as ttk

class YearSelector(Tk):
    def __init__(self, notensys):
        super().__init__()
        self.notensys = notensys
        self.title("Jahr wählen")
        self.geometry("285x100")
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.clean_exit)

        self.years = self.notensys.save_manager.list_saves()
        self.option_var = StringVar(self)
        self.selector = ttk.OptionMenu(self, self.option_var, self.years[0], *self.years)
        self.selector.pack(side=LEFT, padx=20, pady=20)

        self.apply_btn = ttk.Button(self, text="Weiter", command=self.destroy)
        self.apply_btn.pack(side=RIGHT, anchor=SW, padx=(5, 10), pady=(0, 10))

        self.open_folder_btn = ttk.Button(self, text="Ordner öffnen", command=self.notensys.save_manager.open_folder)
        self.open_folder_btn.pack(side=RIGHT, anchor=SW, padx=(10, 0), pady=(0, 10))



        self.mainloop()

    def clean_exit(self):
        raise SystemExit

    def get_selection(self):
        return self.option_var.get()
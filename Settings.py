import tkinter.messagebox
from tkinter import *
import tkinter.ttk as ttk
import shutil, os

# settings dict map
"""
0:  Save path
1:  sorting mode



"""


class Settings(Toplevel):
    def __init__(self, window):
        super().__init__(window)

        self.settings_save = window.notensys.settings_save.copy()

        self.iconbitmap("DATA/icon.ico")
        self.title("Notensys Einstellungen")
        self.geometry("500x300")
        self.resizable(False, False)

        self.window = window
        self.window.settings_open = True
        self.window.settings_instance = self

        self.protocol("WM_DELETE_WINDOW", self.exit)

        self.apply_btn = ttk.Button(self, text="Apply", command=self.apply)
        self.apply_btn.pack(side=BOTTOM, anchor=NE, padx=25, pady=15)

        label = LabelFrame(self, text="Jahr Speicherpfad")
        self.save_path_select = ttk.Entry(label, width=60)
        self.save_path_select.pack()
        self.save_path_select.insert(0, self.settings_save["0"])
        label.pack(padx=5, pady=(5, 0), anchor=W)

    def fill_default_settings(self, notensys):
        notensys.settings_save["0"] = "DATA/Saves"

    def check_values(self, notensys):
        # self.window.notensys.settings_save["0"]
        if notensys.settings_save["1"] == "UNDEFINED":
            notensys.settings_save["1"] = "Alphabetically"

        notensys.settings_save_manager.save(notensys.settings_save)


    def exit(self):
        self.destroy()
        self.window.settings_open = False

    def apply(self):
        self.settings_save["0"] = self.save_path_select.get()
        if self.settings_save["0"] != self.window.notensys.settings_save["0"]:

            # Path to saves changed
            self.window.notensys.save_year()
            tkinter.messagebox.showinfo("Pfad geändert", f"Ein Neustart des Programms ist nötig")
            files = self.window.notensys.save_manager.list_saves()
            for f in files:
                shutil.copy(self.window.notensys.settings_save['0'] + "/" + f, self.settings_save['0'])

        self.window.notensys.settings_save = self.settings_save
        self.window.notensys.settings_save_manager.save(self.window.notensys.settings_save)
        self.exit()

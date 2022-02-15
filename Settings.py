import tkinter.messagebox
from tkinter import *
import tkinter.ttk as ttk
import shutil
from Utils.tkdarktitle import *
from Utils.BlurEnabler import *
from WindowFeatures.HeadlineLabel import *

# settings dict map
"""
0:  Save path
1:  sorting mode
2: Theme DARK/LIGHT
"""


class Settings(Frame):
    def __init__(self, window):
        super().__init__(window)

        self.settings_save = window.notensys.settings_save.copy()
        #self.resizable(False, False)
        #self.grab_set()
        #self.focus_force()

        #self.geometry("500x300")
        #self.iconbitmap("DATA/icon.ico")
        #self.title("Notensys Einstellungen")

        self.window = window
        self.window.settings_open = True
        self.window.settings_instance = self

        #self.protocol("WM_DELETE_WINDOW", self.exit)

        top = Frame(self)
        top.pack(fill=X)

        self.back_btn = ttk.Button(top, text="<", command=self.exit)
        self.back_btn.pack(padx=10, pady=10, side=LEFT)

        self.headline = HeadlineLabel(top, text="Einstellungen")
        self.headline.pack(side=LEFT)

        self.apply_btn = ttk.Button(self, text="Übernehmen", command=self.apply)
        self.apply_btn.pack(side=BOTTOM, anchor=NE, padx=25, pady=15)

        label = ttk.LabelFrame(self, text="Jahr Speicherpfad")
        self.save_path_select = ttk.Entry(label, width=60)
        self.save_path_select.pack()
        self.save_path_select.insert(0, self.settings_save["0"])
        label.pack(padx=5, pady=(5, 0), anchor=W)

        self.dark_mode_var = IntVar()
        self.dark_mode_var.set(self.window.notensys.dark)
        self.dark_mode = ttk.Checkbutton(self, text="Dunkler Modus", style="Switch.TCheckbutton",
                                          variable=self.dark_mode_var)
        self.dark_mode.pack(anchor=W)

        self.blur_var = IntVar()
        self.blur_var.set(self.window.blur_enabled)
        self.blur_swtch = ttk.Checkbutton(self, text="Transparenz (win11 acrylic)", style="Switch.TCheckbutton",
                                             variable=self.blur_var)
        self.blur_swtch.pack(anchor=W)

        self.config(width=self.window.winfo_width(), height=self.window.winfo_height())
        self.pack_propagate(False)
        self.place(x=0, y=0)

        self.upd()

    def upd(self):
        self.config(width=self.window.winfo_width(), height=self.window.winfo_height())
        self.after(100, self.upd)

    def fill_default_settings(self, notensys):
        notensys.settings_save["0"] = "DATA/Saves"

    def check_values(self, notensys):
        # self.window.notensys.settings_save["0"]
        if notensys.settings_save["1"] == "UNDEFINED":
            notensys.settings_save["1"] = "Alphabetically"
        if notensys.settings_save["2"] == "UNDEFINED":
            notensys.settings_save["2"] = "DARK"
        if notensys.settings_save["3"] == "UNDEFINED":
            notensys.settings_save["3"] = False

        notensys.settings_save_manager.save(notensys.settings_save)


    def exit(self):
        self.destroy()
        self.window.settings_open = False

    def apply(self):
        if self.blur_var.get():
            self.settings_save["3"] = True
        else:
            self.settings_save["3"] = False

        if self.dark_mode_var.get():
            if self.settings_save["2"] == "LIGHT":
                self.settings_save["2"] = "DARK"
        else:
            if self.settings_save["2"] == "DARK":
                self.settings_save["2"] = "LIGHT"

        self.settings_save["0"] = self.save_path_select.get()
        if self.settings_save["0"] != self.window.notensys.settings_save["0"]:

            # Path to saves changed
            self.window.notensys.save_year()
            files = self.window.notensys.save_manager.list_saves()
            for f in files:
                shutil.copy(self.window.notensys.settings_save['0'] + "/" + f, self.settings_save['0'])

        self.window.notensys.settings_save = self.settings_save
        self.window.notensys.settings_save_manager.save(self.window.notensys.settings_save)
        self.window.notensys.reload()

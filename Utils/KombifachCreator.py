from Utils.BlurEnabler import enable_blur
from tkinter import *
import tkinter.ttk as ttk
from Utils.tkdarktitle import *
from WindowFeatures.HeadlineLabel import *


class KombifachCreator(Toplevel):
    def __init__(self, window):
        super().__init__()
        self.grab_set()
        self.focus_force()

        self.window = window

        self.resizable(False, False)
        if window.notensys.dark:
            try:
                dark_title_bar(self)
            except:
                pass

        self.iconbitmap("DATA/icon.ico")
        self.title("Geschichte/Sozi kombinieren")
        self.geometry("420x300")

        if window.notensys.dark:
            self.config(bg="#1c1c1c")
            if window.blur_enabled:
                try:
                    enable_blur(self)
                except:
                    pass

        self.apply_btn = ttk.Button(self, style="Accent.TButton", text="Erstellen", command=self.apply)
        self.apply_btn.pack(anchor=E, padx=10, pady=10, side=BOTTOM)

        instruction_frame = ttk.Label(self, text="Dieses Fenster erstellt dir ein Kombifach Geschichte/Sozi aus den beiden Fächern", wraplengt=200)
        instruction_frame.pack(side=RIGHT, padx=10, pady=10, anchor=NE)

        HeadlineLabel(self, text="Geschichte wählen").pack(anchor=NW, padx=10, pady=10)

        self.years = self.window.notensys.save["subjects"]
        self.option_varges = StringVar(self)
        self.selector_ges = ttk.OptionMenu(self, self.option_varges, self.years[0], *self.years)
        self.selector_ges.pack(padx=(20, 0), pady=(0, 20), anchor=NW)

        HeadlineLabel(self, text="Sozialkunde wählen").pack(anchor=NW, padx=10, pady=10)

        self.years = self.window.notensys.save["subjects"]
        self.option_varsk = StringVar(self)
        self.selector_sk = ttk.OptionMenu(self, self.option_varsk, self.years[0], *self.years)
        self.selector_sk.pack(padx=(20, 0), pady=(0, 20), anchor=NW)

    def apply(self):
        try:
            self.window.notensys.rem_subject("New")
        except:
            pass
        self.window.notensys.add_subject()

        ges = self.option_varges.get()
        sk = self.option_varsk.get()

        self.window.notensys.save["grades"][ges]["NBT"]["is_ges"] = True
        self.window.notensys.save["grades"][sk]["NBT"]["is_sk"] = True
        self.window.notensys.rename_subject("New", "Geschichte/Sozi")
        self.window.notensys.save["grades"]["Geschichte/Sozi"]["NBT"]["sk_gs_kombi"] = True


        self.window.subject_overview.redraw()
        self.destroy()


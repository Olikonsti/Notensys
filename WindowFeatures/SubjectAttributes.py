from tkinter import *
import tkinter.ttk as ttk
from WindowFeatures.HeadlineLabel import HeadlineLabel


class SubjectAttributes(ttk.Frame):
    def __init__(self, window, notensys):
        super().__init__(window, width=300, height=200)
        HeadlineLabel(self, text="Attribute").pack(anchor=W)
        self.interior = Frame(self)
        self.interior.pack(expand=True, fill=BOTH)


    def clear(self):
        self.interior.destroy()
        self.interior = Frame(self)
        self.interior.pack(expand=True, fill=BOTH, pady=(0, 10))
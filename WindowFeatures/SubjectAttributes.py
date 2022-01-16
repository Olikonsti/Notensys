from tkinter import *
import tkinter.ttk as ttk

class SubjectAttributes(ttk.LabelFrame):
    def __init__(self, window, notensys):
        super().__init__(window, text="Attribute", width=300, height=200)
        self.interior = Frame(self)
        self.interior.pack(expand=True, fill=BOTH)


    def clear(self):
        self.interior.destroy()
        self.interior = Frame(self)
        self.interior.pack(expand=True, fill=BOTH)
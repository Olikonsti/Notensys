from tkinter import *
import tkinter.ttk as ttk

class SubjectAttributes(LabelFrame):
    def __init__(self, window, notensys):
        super().__init__(window, text="Attribute", width=300, height=200, fg=notensys.text_color, bg=notensys.bg_color)
        self.interior = Frame(self)
        self.interior.pack(expand=True, fill=BOTH)


    def clear(self):
        self.interior.destroy()
        self.interior = Frame(self)
        self.interior.pack(expand=True, fill=BOTH)
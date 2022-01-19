from tkinter import *
import tkinter.ttk as ttk

class TitleBarMenuItem(Menubutton):
    def __init__(self, parent, notensys, text):
        super().__init__(parent)
        self.config(text=text, relief=FLAT, activebackground=notensys.bg_color, activeforeground=notensys.text_color, bg=notensys.bg_color)
        self.pack(side=LEFT, )

class TitleBarItem(Button):
    def __init__(self, parent, notensys, text, command=None,):
        super().__init__(parent)
        self.config(text=text, relief=FLAT, activebackground=notensys.bg_color, activeforeground=notensys.text_color, bg=notensys.bg_color)
        self.pack(side=LEFT)

        if command != None:
            self.config(command=command)
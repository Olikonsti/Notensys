from tkinter import *
import tkinter.ttk as ttk

class HeadlineLabel(Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config(font="Helvetica 14")
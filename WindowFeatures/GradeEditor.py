from tkinter import *
import tkinter.ttk as ttk
from WindowFeatures.GradeList import *

class GradeEditor(Toplevel):
    def __init__(self, parent, subject, notensys):
        super().__init__(parent)

        self.window = parent
        self.notensys = notensys
        self.subject = subject
        self.resizable(False, False)

        self.geometry("500x700")

        self.title(f"Noten für {self.subject} editieren")


        self.top_frame = GradeList(self, text="Mündliche Noten", grades={"yee": 1, "yaa": 2}, subject=subject, notensys=notensys, mode="small")

        self.bottom_frame = GradeList(self, text="Klausur Noten", grades={"lelel": 1, "lalala": 2}, subject=subject, notensys=notensys, mode="big")
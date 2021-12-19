from tkinter import *
import tkinter.ttk as ttk
from WindowFeatures.GradeList import *

class GradeEditor(Frame):
    def __init__(self, parent, subject, notensys):
        super().__init__(parent, width=300)

        self.notensys = notensys
        self.subject = subject

        try:
            self.notensys.window.active_grade_editor.destroy()
        except:
            pass

        self.notensys.window.active_grade_editor = self

        #self.resizable(False, False)
        #self.iconbitmap("DATA/icon.ico")

        #self.geometry("500x700")

        #self.title(f"Noten für {self.subject} editieren")


        self.top_frame = GradeList(self, text="Kleine Leistungsnachweise", grades={}, subject=subject, notensys=notensys, mode="small")

        self.bottom_frame = GradeList(self, text="Große Leistungsnachweise", grades={}, subject=subject, notensys=notensys, mode="big")

        self.pack(fill=BOTH, expand=True)
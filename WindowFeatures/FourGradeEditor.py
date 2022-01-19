from tkinter import *
import tkinter.ttk as ttk
from WindowFeatures.GradeList import *

class FourGradeEditor(Frame):
    def __init__(self, parent, subject, notensys):
        super().__init__(parent)

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

        self.notensys.window.expanded = True
        self.notensys.window.change_geometry_width(260)

        l1 = ttk.LabelFrame(self)
        l1.pack(side=LEFT, fill=BOTH, expand=True)

        l2 = ttk.LabelFrame(self)
        l2.pack(side=RIGHT, fill=BOTH, expand=True)
        self.top_frame = GradeList(l1, text="Kleine Leistungsnachweise", grades={}, subject=subject, notensys=notensys, mode="small")

        self.bottom_frame = GradeList(l1, text="Große Leistungsnachweise", grades={}, subject=subject, notensys=notensys, mode="big")

        self.bottom_frame = GradeList(l2, text="Große Leistungsnachweise", grades={}, subject=subject,
                                      notensys=notensys, mode="big")

        self.bottom_frame = GradeList(l2, text="Große Leistungsnachweise", grades={}, subject=subject,
                                      notensys=notensys, mode="big")

        self.pack(fill=BOTH, expand=True)
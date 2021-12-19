from tkinter import *
import tkinter.ttk as ttk

from WindowFeatures.SubjectOverview import *
from WindowFeatures.SubjectAttributes import *

class Window(Tk):
    def __init__(self, notensys):
        super().__init__()
        self.notensys = notensys
        self.title("Notensys Übersicht")
        self.geometry("600x500")
        #self.resizable(False, True)
        self.iconbitmap("DATA/icon.ico")

        self.active_grade_editor = None

        self.update()
        self.notensys.window = self

        self.topbar = Frame(self)
        self.topbar.pack(fill=X)

        self.subject_overview = SubjectOverview(self, notensys)

        self.rightPane = Frame(self, width=300)
        self.rightPane.pack(side=RIGHT, fill=Y, padx=5, pady=(0, 5))

        self.subject_attributes = SubjectAttributes(self.rightPane, self.notensys)
        self.subject_attributes.pack(fill=BOTH, expand=True)

        self.bottom_right_pane = LabelFrame(self.rightPane, text="Leistungsnachweise", width=300, height=1000)
        self.bottom_right_pane.pack_propagate(False)
        self.bottom_right_pane.pack(fill=BOTH, expand=True)

        self.protocol("WM_DELETE_WINDOW", self.notensys.save_year_exit)

        self.update()





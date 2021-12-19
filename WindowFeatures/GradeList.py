import tkinter.messagebox

from VerticalScrolledFrame import *
from tkinter import *
import tkinter.ttk as ttk

from WindowFeatures.GradeListElement import *

class GradeList(LabelFrame):
    def __init__(self, parent, text, grades, subject, notensys, mode):
        super().__init__(parent, text=text, height=200)
        self.parent = parent
        self.notensys = notensys

        self.pack(fill=X, padx=5, pady=5)

        self.items_displayed = []
        self.selected = None

        self.topbar = Frame(self)
        self.topbar.pack(fill=X)

        self.add_btn = ttk.Button(self.topbar, text="+", width=4, command=self.add_dialog)
        self.add_btn.pack(side=LEFT)

        self.rem_btn = ttk.Button(self.topbar, text="-", width=4, command=self.rem_grade)
        self.rem_btn.pack(side=LEFT)


        self.scrollarea = VerticalScrolledFrame(self)
        self.scrollarea.pack(fill=BOTH, expand=True)

        self.grades = notensys.save["grades"][subject][mode]
        for i in self.grades:
            GradeListElement(self.scrollarea.interior, self, i, self.grades[i])

    def rem_grade(self):
        if self.selected != None:
            del self.grades[self.selected.grade_text]
            self.selected = None
            self.redraw()

    def add_dialog(self):
        self.win = Toplevel(self.parent)
        self.win.iconbitmap("DATA/icon.ico")
        self.win.title("Note hinzufügen")
        self.win.resizable(False, False)
        self.win.geometry("300x120")

        self.lf = LabelFrame(self.win, text="Notiz")
        self.name_entry = ttk.Entry(self.lf)
        self.name_entry.pack()
        self.lf.pack(anchor=NW)

        self.lf = LabelFrame(self.win, text="Punkte")
        self.grade_entry = ttk.Entry(self.lf)
        self.grade_entry.pack()
        self.lf.pack(anchor=NW)

        self.apply_btn = ttk.Button(self.win, text="Ok", command=self.apply)
        self.apply_btn.pack(anchor=NE)

    def apply(self):
        if self.name_entry.get() not in self.grades and self.grade_entry.get().isnumeric():
            self.grades[self.name_entry.get()] = int(self.grade_entry.get())
            self.win.destroy()
        else:
            tkinter.messagebox.showinfo("Kann Objekt nicht erstellen", "Es existiert bereits ein Objekt mit dieser Notiz.")
        self.redraw()


    def redraw(self):
        for i in self.items_displayed:
            i.destroy()
        self.items_displayed.clear()
        for i in self.grades:
            GradeListElement(self.scrollarea.interior, self, i, self.grades[i])

        self.notensys.window.subject_overview.redraw()






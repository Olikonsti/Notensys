import tkinter.messagebox
from Utils.tkdarktitle import *

from Utils.VerticalScrolledFrame import *

from WindowFeatures.GradeListElement import *
from WindowFeatures.HeadlineLabel import *

class GradeList(ttk.Frame):
    def __init__(self, parent, text, grades, subject, notensys, mode):
        super().__init__(parent, height=100)
        self.parent = parent
        self.notensys = notensys

        HeadlineLabel(parent, text=text).pack(anchor=NW, padx=5, pady=(5, 0))

        self.pack(fill=BOTH, expand=True, padx=5, pady=5)
        self.pack_propagate(False)

        self.items_displayed = []
        self.selected = None

        self.topbar = Frame(self)
        self.topbar.pack(fill=X, pady=(0, 5))

        self.add_btn = ttk.Button(self.topbar, text="+", width=4, command=self.add_dialog)
        self.add_btn.pack(side=LEFT, padx=3)

        self.rem_btn = ttk.Button(self.topbar, text="-", width=4, command=self.rem_grade)
        self.rem_btn.pack(side=LEFT, padx=3)

        self.edit_btn = ttk.Button(self.topbar, text="Edit", width=4, command=self.edit_grade)
        self.edit_btn.pack(side=LEFT, padx=3)


        self.scrollarea = VerticalScrolledFrame(self, height=100)
        self.scrollarea.interior.config(height=100)
        self.scrollarea.canvas.config(height=2000)
        self.scrollarea.canvas.pack(side=LEFT, fill=BOTH)
        self.scrollarea.pack(fill=BOTH)

        self.grades = notensys.save["grades"][subject][mode]
        for i in self.grades:
            GradeListElement(self.scrollarea.interior, self, i, self.grades[i])

    def edit_grade(self):
        if self.selected == None:
            return 0
        self.win = Toplevel(self.parent)
        dark_title_bar(self.win)
        self.win.grab_set()
        self.win.focus_force()
        self.win.iconbitmap("DATA/icon.ico")
        self.win.title("Note ändern")
        self.win.resizable(False, False)
        dark_title_bar(self.win)
        self.win.geometry("250x170")



        self.lf = ttk.LabelFrame(self.win, text="Notiz")
        self.name_entry = ttk.Entry(self.lf)
        self.name_entry.pack()
        self.name_entry.insert(0, self.selected.grade_text)
        self.lf.pack(anchor=NW, padx=5, pady=(5, 0))

        self.lf = ttk.LabelFrame(self.win, text="Punkte")
        self.grade_entry = ttk.Entry(self.lf)
        self.grade_entry.pack()
        self.grade_entry.insert(0, self.grades[self.selected.grade_text])
        self.lf.pack(anchor=NW, padx=5, pady=(5, 0))

        self.apply_btn = ttk.Button(self.win, text="Ok", command=self.apply_edit)
        self.apply_btn.pack(anchor=NE)

    def apply_edit(self):
        if self.selected != None:
            del self.grades[self.selected.grade_text]
            self.selected = None
        else:
            return 0

        if self.name_entry.get() not in self.grades and self.grade_entry.get().isnumeric():
            self.grades[self.name_entry.get()] = int(self.grade_entry.get())
            self.win.destroy()
        else:
            tkinter.messagebox.showinfo("Kann Objekt nicht erstellen", "Es existiert bereits ein Objekt mit dieser Notiz.")
        self.redraw()

    def rem_grade(self):
        if self.selected != None:
            del self.grades[self.selected.grade_text]
            self.selected = None
            self.redraw()

    def add_dialog(self):
        self.win = Toplevel(self.parent)
        self.win.grab_set()
        self.win.focus_force()

        self.win.resizable(False, False)
        dark_title_bar(self.win)
        self.win.iconbitmap("DATA/icon.ico")
        self.win.title("Note hinzufügen")
        self.win.geometry("250x170")
        self.lf = ttk.LabelFrame(self.win, text="Notiz")
        self.name_entry = ttk.Entry(self.lf)
        self.name_entry.pack()
        self.lf.pack(anchor=NW, padx=5, pady=(5, 0))

        self.lf = ttk.LabelFrame(self.win, text="Punkte")
        self.grade_entry = ttk.Entry(self.lf)
        self.grade_entry.pack()
        self.lf.pack(anchor=NW, padx=5, pady=(5, 0))

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








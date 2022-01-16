from VerticalScrolledFrame import *
from tkinter import *
import tkinter.ttk as ttk

from WindowFeatures.ColorIndicator import *
from WindowFeatures.GradeEditor import *


class SubjectOverviewElement(Frame):
    def __init__(self, subject_overview, subject, notensys):
        super().__init__(subject_overview.scrollarea.interior, highlightthickness=1)
        self.selected = False
        self.notensys = notensys
        self.window = notensys.window
        self.subject_overview = subject_overview
        self.subject = subject
        self.subject_overview.subjects_displayed.append(self)

        self.subject_name = Label(self, text=subject, fg=self.notensys.text_color)
        self.subject_name.pack(side=LEFT)

        self.color_indicator = ColorIndicator(self, points=notensys.calculate_average(subject))
        self.color_indicator.place(relx=0.4, rely=0.15)

        self.point_average = Label(self, text=notensys.calculate_average(subject), fg=self.notensys.text_color)
        self.point_average.place(relx=0.8, y=0)

        #self.test = Label(self, text=6-(notensys.calculate_average(subject)/3))
        #self.test.place(relx=0.2, y=0)

        # bind select toggler
        self.bind("<Button-1>", self.toggle_select)
        self.subject_name.bind("<Button-1>", self.toggle_select)
        self.color_indicator.bind("<Button-1>", self.toggle_select)
        self.point_average.bind("<Button-1>", self.toggle_select)

        self.pack(fill=X, pady=2)
        self.deselect()

    def toggle_select(self, event=None):
        if self.selected:
            self.deselect()
        else:
            self.select()

    def select(self):
        try:
            self.notensys.window.active_grade_editor.destroy()
        except:
            pass
        self.subject_attributes = self.window.subject_attributes
        for i in self.subject_overview.subjects_displayed:
            i.deselect()
        self.subject_overview.selected = self
        self.selected = True
        self.editMenu(self.subject_attributes.interior,)
        self.subject_name.config(bg=self.notensys.bg_select, fg=self.notensys.text_color)
        self.point_average.config(bg=self.notensys.bg_select, fg=self.notensys.text_color)
        self.config(bg=self.notensys.bg_select, highlightbackground=self.notensys.highlight_color, highlightcolor=self.notensys.highlight_color, highlightthickness=1)

    def deselect(self):
        try:
            self.notensys.window.active_grade_editor.destroy()
        except:
            pass
        self.subject_overview.selected = None
        try:
            self.window.subject_attributes.clear()
        except:
            pass
        self.selected = False
        self.subject_name.config(bg=self.notensys.bg_color)
        self.point_average.config(bg=self.notensys.bg_color)
        self.config(bg=self.notensys.bg_color, highlightbackground="#ABABAB", highlightcolor="#ABABAB")

    def editMenu(self, parent):
        self.name_entry = ttk.Entry(parent)
        self.name_entry.pack(anchor=NW, padx=5, pady=5)
        self.name_entry.insert(0, self.subject)

        btn_frame = Frame(parent)
        btn_frame.pack(side=BOTTOM, fill=X)

        self.apply_btn = ttk.Button(btn_frame, text="Speichern", command=self.upd_data)
        self.apply_btn.pack(side=RIGHT, anchor=NW, padx=(5, 5), pady=5)

        GradeEditor(self.window.bottom_right_pane, self.subject, self.notensys)

    def upd_data(self):
        self.notensys.rename_subject(self.subject, self.name_entry.get())


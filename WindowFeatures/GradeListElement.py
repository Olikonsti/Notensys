from tkinter import *
import tkinter.ttk as ttk

from WindowFeatures.ColorIndicator import *

class GradeListElement(Frame):
    def __init__(self, parent, gradelist, grade_text, grade_points):
        super().__init__(parent, highlightthickness=1)
        self.selected = False
        self.grade_text = grade_text
        self.gradelist = gradelist
        self.notensys = self.gradelist.notensys
        self.gradelist.items_displayed.append(self)

        self.notiz = Label(self, text=grade_text, fg=self.notensys.text_color)
        self.notiz.pack(side=LEFT)

        self.color_indicator = ColorIndicator(self, points=grade_points)
        self.color_indicator.place(relx=0.56, rely=0.15)

        self.points = Label(self, text=grade_points, fg=self.notensys.text_color)
        self.points.place(relx=0.9, y=0)

        self.pack(fill=X, pady=2, padx=(5, 1))

        self.deselect()

        self.bind("<Button-1>", self.toggle_select)
        self.notiz.bind("<Button-1>", self.toggle_select)
        self.color_indicator.bind("<Button-1>", self.toggle_select)
        self.points.bind("<Button-1>", self.toggle_select)


    def toggle_select(self, event=None):
        if self.selected:
            self.deselect()
        else:
            self.select()

    def select(self):
        for i in self.gradelist.items_displayed:
            i.deselect()
        self.selected = True
        self.gradelist.selected = self

        self.notiz.config(bg=self.notensys.bg_select, fg=self.notensys.text_color)
        self.points.config(bg=self.notensys.bg_select, fg=self.notensys.text_color)
        self.config(bg=self.notensys.bg_select, highlightbackground=self.notensys.highlight_color_selected,
                    highlightcolor=self.notensys.highlight_color_selected, highlightthickness=1)

    def deselect(self):
        self.gradelist.selected = None
        self.selected = False
        self.notiz.config(bg=self.notensys.bg_color)
        self.points.config(bg=self.notensys.bg_color)
        self.config(bg=self.notensys.bg_color, highlightbackground=self.notensys.highlight_color, highlightcolor=self.notensys.highlight_color)


from tkinter import *
import tkinter.ttk as ttk

from WindowFeatures.ColorIndicator import *

class GradeListElement(Frame):
    def __init__(self, parent, gradelist, grade_text, grade_points):
        super().__init__(parent, highlightthickness=1)
        self.selected = False
        self.grade_text = grade_text
        self.gradelist = gradelist
        self.gradelist.items_displayed.append(self)

        self.notiz = Label(self, text=grade_text)
        self.notiz.pack(side=LEFT)

        self.color_indicator = ColorIndicator(self, points=grade_points)
        self.color_indicator.place(x=100, y=2)

        self.points = Label(self, text=grade_points)
        self.points.place(x=220, y=0)

        self.pack(fill=X, pady=2)

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

        self.notiz.config(bg="#D8E6F1")
        self.points.config(bg="#D8E6F1")
        self.config(bg="#D8E6F1", highlightbackground="#0078D4", highlightcolor="#0078D4", highlightthickness=1)

    def deselect(self):
        self.gradelist.selected = None
        self.selected = False
        self.notiz.config(bg="#F0F0F0")
        self.points.config(bg="#F0F0F0")
        self.config(bg="#F0F0F0", highlightbackground="#ABABAB", highlightcolor="#ABABAB")


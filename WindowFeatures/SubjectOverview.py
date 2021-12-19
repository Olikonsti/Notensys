from VerticalScrolledFrame import *
from tkinter import *
import tkinter.ttk as ttk

from WindowFeatures.SubjectOverviewElement import *


class SubjectOverview(LabelFrame):
    def __init__(self, window, notensys):
        super().__init__(window, text="Fächer", width=300)

        self.subjects_displayed = []
        self.selected = None

        self.notensys = notensys

        self.topbar = Frame(self)
        self.topbar.pack(fill=X)

        self.add_btn = ttk.Button(self.topbar, text="+", width=4, command=notensys.add_subject)
        self.add_btn.pack(side=LEFT)

        self.rem_btn = ttk.Button(self.topbar, text="-", width=4, command=lambda: notensys.rem_subject(self.selected.subject))
        self.rem_btn.pack(side=LEFT)


        self.scrollarea = VerticalScrolledFrame(self)
        self.scrollarea.pack(expand=True, fill=BOTH)

        self.pack(side=LEFT, fill=BOTH, expand=True, padx=(5, 0), pady=(0, 5))

        self.redraw()

    def redraw(self):
        for i in self.subjects_displayed:
            i.destroy()
        self.subjects_displayed.clear()
        for i in self.notensys.save["subjects"]:
            SubjectOverviewElement(self, i, self.notensys)

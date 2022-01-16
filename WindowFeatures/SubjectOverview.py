from VerticalScrolledFrame import *
from tkinter import *
import tkinter.ttk as ttk
from BubbleSort import bubble_sort

from WindowFeatures.SubjectOverviewElement import *


class SubjectOverview(ttk.LabelFrame):
    def __init__(self, window, notensys):
        super().__init__(window, text="Fächer", width=300)

        self.subjects_displayed = []
        self.selected = None

        self.notensys = notensys

        self.topbar = Frame(self)
        self.topbar.pack(fill=X, pady=(0, 5))

        self.add_btn = ttk.Button(self.topbar, text="+", width=4, command=notensys.add_subject)
        self.add_btn.pack(side=LEFT, padx=3)

        self.rem_btn = ttk.Button(self.topbar, text="-", width=4, command=lambda: notensys.rem_subject(self.selected.subject))
        self.rem_btn.pack(side=LEFT, padx=3)

        self.sort_methods = ["Alphabetisch", "0 - 15", "15 - 0"]
        self.sort_var = StringVar(self)
        self.selector = ttk.OptionMenu(self.topbar, self.sort_var, self.notensys.settings_save["1"], *self.sort_methods, command=self.sort_subjects)
        self.selector.pack(side=LEFT, padx=3)
        self.selector["menu"].config(bg=notensys.bg_color, fg=notensys.text_color)




        self.scrollarea = VerticalScrolledFrame(self)
        self.scrollarea.pack(expand=True, fill=BOTH)

        self.pack(side=LEFT, fill=BOTH, expand=True, padx=(5, 0), pady=(0, 5))
        self.sort_subjects(mode_=self.notensys.settings_save["1"])

    def sort_subjects(self, event=None, mode_=None):
        mode = self.sort_var.get()
        if mode_ != None:
            mode = mode_
        if mode == "Alphabetisch":
            self.notensys.save["subjects"] = sorted(self.notensys.save["subjects"])
            self.notensys.settings_save["1"] = "Alphabetisch"
            self.notensys.settings_save_manager.save()
        elif mode == "0 - 15":
            bubble_sort(self.notensys.save["subjects"], notensys=self.notensys)
            self.notensys.settings_save["1"] = "0 - 15"
            self.notensys.settings_save_manager.save()
        elif mode == "15 - 0":
            self.notensys.settings_save["1"] = "15 - 0"
            self.notensys.settings_save_manager.save()
            bubble_sort(self.notensys.save["subjects"], notensys=self.notensys, reversed=True)

        else:
            self.notensys.save["subjects"] = sorted(self.notensys.save["subjects"])
        self.redraw()


    def redraw(self):
        selected = self.selected
        for i in self.subjects_displayed:
            i.destroy()
        self.subjects_displayed.clear()
        for i in self.notensys.save["subjects"]:
            SubjectOverviewElement(self, i, self.notensys)
        for i in self.subjects_displayed:
            if selected != None:
                if selected.subject == i.subject:
                    i.select()

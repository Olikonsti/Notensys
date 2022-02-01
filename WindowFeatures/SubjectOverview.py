from Utils.BubbleSort import bubble_sort

from WindowFeatures.SubjectOverviewElement import *
from WindowFeatures.SubjectOverviewKomiElement import *


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

        avg = self.notensys.calculate_whole_average()
        self.average_label = ttk.Label(self.topbar, text=f"Schnitt: {avg}")
        self.average_label.pack(side=LEFT, padx=3)

        self.average_color_indicator = ColorIndicator(self.topbar, avg)
        self.average_color_indicator.pack(side=LEFT, padx=4)

        self.scrollarea = VerticalScrolledFrame(self)
        self.scrollarea.pack(expand=True, fill=BOTH, padx=(0, 5))

        self.pack(side=LEFT, fill=BOTH, expand=True, padx=(5, 0), pady=(0, 5))
        self.sort_subjects(mode_=self.notensys.settings_save["1"])

    def update_average_label(self):
        avg = self.notensys.calculate_whole_average()
        self.average_label.config(text=f"Schnitt: {avg}")
        self.average_color_indicator.destroy()
        self.average_color_indicator = ColorIndicator(self.topbar, avg)
        self.average_color_indicator.pack(side=LEFT, padx=4)

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


    def redraw(self, blured_already=False):
        selected = self.selected
        for i in self.subjects_displayed:
            i.destroy()
        self.subjects_displayed.clear()

        for i in self.notensys.save["subjects"]:
            if "sk_gs_kombi" in self.notensys.save["grades"][i]["NBT"]:
                SubjectOverviewKombiElement(self, i, self.notensys)
            else:
                if not "is_sk" in self.notensys.save["grades"][i]["NBT"] and not "is_ges" in self.notensys.save["grades"][i]["NBT"]:    # wenn nicht sozialkunde oder geschichte in kombifach
                    SubjectOverviewElement(self, i, self.notensys)
        for i in self.subjects_displayed:
            if selected != None:
                if selected.subject == i.subject:
                    i.select()
        self.update_average_label()

    def select_subject(self, subject):
        for i in self.subjects_displayed:
            if i.subject == subject:
                i.select()

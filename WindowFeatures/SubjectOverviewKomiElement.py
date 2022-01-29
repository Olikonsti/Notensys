from WindowFeatures.GradeEditor import *
from WindowFeatures.SubjectOverviewElement import *
import math

class SubjectOverviewKombiElement(Frame):
    def __init__(self, subject_overview, subject, notensys):
        super().__init__(subject_overview.scrollarea.interior, highlightthickness=1)
        self.selected = False
        self.is_kombi = True
        self.is_in_kombi = False
        self.notensys = notensys
        self.window = notensys.window
        self.subject_overview = subject_overview
        self.subject = subject
        self.subject_overview.subjects_displayed.append(self)

        self.subjects_displayed = []
        self.subjects_in_kombi = []
        self.place_interior()
        self.in_frame_wdgts = []

        self.expand_icon = Label(self, text="▼", font="Helvetica 10", fg=self.notensys.text_color)
        self.expand_icon.place(relx=0.9, y=0)
        self.in_frame_wdgts.append(self.expand_icon)

        self.subject_name = Label(self, text=subject, fg=self.notensys.text_color)
        self.subject_name.pack(side=TOP, anchor=NW)
        self.in_frame_wdgts.append(self.subject_name)

        avg = self.calc_avg()
        try:
            self.color_indicator = ColorIndicator(self, points=avg)
            self.color_indicator.place(relx=0.4, y=4)

            self.point_average = Label(self, text=avg, fg=self.notensys.text_color)
            self.point_average.place(relx=0.8, y=0)
            self.in_frame_wdgts.append(self.point_average)

            self.color_indicator.bind("<Button-1>", self.toggle_select)
            self.point_average.bind("<Button-1>", self.toggle_select)
        except:
            pass

        #self.test = Label(self, text=6-(notensys.calculate_average(subject)/3))
        #self.test.place(relx=0.2, y=0)

        # bind select toggler
        self.bind("<Button-1>", self.toggle_select)
        self.subject_name.bind("<Button-1>", self.toggle_select)
        self.expand_icon.bind("<Button-1>", self.toggle_select)


        self.pack(fill=X, pady=2, padx=(5, 1))
        self.deselect()

    def place_interior(self):
        self.interior = Frame(self, height=20, bg=self.notensys.bg_select)
        self.interior.pack(fill=X, padx=(20, 0), pady=5)
        for i in self.notensys.save["grades"]:
            if "is_sk" in self.notensys.save["grades"][i]["NBT"] or "is_ges" in self.notensys.save["grades"][i]["NBT"]:
                SubjectOverviewElement(self, i, self.notensys, is_in_kombi=True)
                self.subjects_in_kombi.append(i)

    def deselect_items(self):
        for i in self.subjects_displayed:
            i.deselect()

    def calc_avg(self):
        ges_grade = '   -'
        sk_grade = '   -'
        for i in self.subjects_in_kombi:
            try:
                grade = int(self.notensys.calculate_average(i)+0.5) # round down at .5
            except:
                grade = '   -'
            if "is_ges" in self.notensys.save["grades"][i]["NBT"]:
                ges_grade = grade
            if "is_sk" in self.notensys.save["grades"][i]["NBT"]:
                sk_grade = grade

        if ges_grade == '   -':
            avg = sk_grade
        elif sk_grade == '   -':
            avg = ges_grade
        elif sk_grade == '   -' and ges_grade == '   -':
            avg = '   -'
        else:
            avg = round((sk_grade+ges_grade+ges_grade)/3, 2)
        self.notensys.save["grades"][self.subject]["big"] = {"KOMBI": avg}
        return avg

    def clear_interior(self):
        try:
            self.interior.destroy()
        except:
            pass

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
        self.config(height=40)
        self.subject_overview.selected = self
        self.selected = True
        self.place_interior()
        self.expand_icon["text"] = "▲"
        for i in self.in_frame_wdgts:
            i.config(bg=self.notensys.bg_select, fg=self.notensys.text_color)
        self.config(bg=self.notensys.bg_select, highlightbackground=self.notensys.highlight_color_selected, highlightcolor=self.notensys.highlight_color_selected, highlightthickness=1)

    def deselect(self):
        self.clear_interior()
        self.config(height=0)
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
        self.expand_icon["text"] = "▼"
        for i in self.in_frame_wdgts:
            i.config(bg=self.notensys.bg_color, fg=self.notensys.text_color)
        self.config(bg=self.notensys.bg_color, highlightbackground=self.notensys.highlight_color, highlightcolor=self.notensys.highlight_color)



from SaveManager import *
from Window import *
from YearSelector import *
from SplashScreen import *
from tkinter import messagebox


class Notensys():
    def __init__(self):
        self.version = "dev_1.0"
        SplashScreen(self)
        self.save_manager = SaveManager(self)
        self.save = {
            "subjects": ["Mathe"],
            "grades": {
                "Mathe": {
                    "small": {"ausfrage": 3, "ex": 4},
                    "big": {}
                },
            }
        }

        self.year_selector = YearSelector(self)
        self.selected_year = self.year_selector.get_selection()
        self.save = self.save_manager.load(self.selected_year)
        self.window = Window(self)
        self.window.mainloop()

    def save_year_exit(self):
        print("Saving...")
        self.save_manager.save(self.selected_year, self.save)
        raise SystemExit


    def add_subject(self):
        for i in self.save["subjects"]:
            if i == "New":
                messagebox.showinfo("Kann kein neues Element erstellen", "Ein Element mit dem Namen existiert bereits.")
                return 0
        self.save["subjects"].append("New")
        self.save["grades"]["New"] = {"small": {}, "big": {}}

        self.window.subject_overview.redraw()

    def rem_subject(self, name):
        if name != None:
            self.save["subjects"].remove(name)
            del self.save["grades"][name]
        self.window.subject_overview.redraw()

    def rename_subject(self, old, new, redraw=True):

        for i in self.save["subjects"]:
            if i == new:
                messagebox.showinfo("Kann kein neues Element erstellen", "Ein Element mit dem Namen existiert bereits.")
                return 0

        temp_grades = self.save["grades"][old]

        self.save["subjects"].remove(old)
        del self.save["grades"][old]

        self.save["subjects"].append(new)
        self.save["grades"][new] = temp_grades
        if redraw:
            self.window.subject_overview.redraw()

    def calculate_average(self, subject):
        avg_small = 0
        grade_sum = 0
        grade_count = 0
        for i in self.save["grades"][subject]["small"]:
            grade_count += 1
            grade_sum += self.save["grades"][subject]["small"][i]
        try:
            avg_small = grade_sum/grade_count
        except:
            avg_small = -1

        avg_big = 0
        grade_sum = 0
        grade_count = 0
        for i in self.save["grades"][subject]["big"]:
            grade_count += 1
            grade_sum += self.save["grades"][subject]["big"][i]
        try:
            avg_big = grade_sum / grade_count
        except:
            avg_big = -1

        try:
            if avg_big == -1:
                avg = avg_small
            elif avg_small == -1:
                avg = avg_big
            else:
                avg = (avg_small + avg_big)/2
        except:
            avg = "NA"

        return avg
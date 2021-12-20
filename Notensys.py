
from SaveManager import *
from Window import *
from YearSelector import *
from SplashScreen import *
from tkinter import messagebox
import os.path


class Notensys():
    def __init__(self):
        self.version = "2.3"
        self.version_date = "20.12.2021"
        SplashScreen(self)
        self.save_manager = SaveManager(self)
        self.save = {
            "subjects": ["Mathe"],
            "grades": {
                "Mathe": {
                    "small": {"ausfrage": 13, "ex": 14},
                    "big": {}
                },
            }
        }

        if len(self.save_manager.list_saves()) < 1:
            self.save_manager.save("11_1", self.save)
            self.save_manager.save("11_2", self.save)
            self.save_manager.save("12_1", self.save)
            self.save_manager.save("12_2", self.save)
        """
        # load settings file
        if os.path.isfile('DATA/settings.txt'):
            f = open("DATA/settings.txt")
            print(f.read())
            f.close()
        else:
            f = open("DATA/settings.txt", "w")
            f.write("yeet")
            f.close()
        """

        self.year_selector = YearSelector(self)
        self.selected_year = self.year_selector.get_selection()
        self.save = self.save_manager.load(self.selected_year)
        self.window = Window(self)
        self.window.mainloop()

    def open_year_selector(self):
        self.year_selector = YearSelector(self)
        self.selected_year = self.year_selector.get_selection()
        self.save = self.save_manager.load(self.selected_year)
        self.window = Window(self)

    def save_year_exit(self):
        print("Saving...")
        self.save_manager.save(self.selected_year, self.save)
        raise SystemExit

    def save_year(self):
        print("Saving...")
        self.save_manager.save(self.selected_year, self.save)


    def add_subject(self):
        for i in self.save["subjects"]:
            if i == "New":
                messagebox.showinfo("Kann kein neues Element erstellen", "Ein Element mit dem Namen existiert bereits.")
                return 0
        self.save["subjects"].append("New")
        self.save["grades"]["New"] = {"small": {}, "big": {}}

        self.window.subject_overview.redraw()

        for i in self.window.subject_overview.subjects_displayed:
            if i.subject == "New":
                i.select()



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
                avg = round(avg_small, 2)
            elif avg_small == -1:
                avg = round(avg_big, 2)
            else:
                avg = round((avg_small + avg_big)/2, 2)
            if avg_small == -1 and avg_big == -1:
                avg = "   -"
        except:
            avg = "NA"

        return avg
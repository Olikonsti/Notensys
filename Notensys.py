
from SaveManager import *
from SettingsSaveManager import *
from Window import *
from YearSelector import *
from SplashScreen import *
from tkinter import messagebox
import os.path


class Notensys():
    def __init__(self):
        self.version = "3.3"
        self.version_date = "16.01.2022"
        self.splash_screen = SplashScreen(self)
        self.splash_screen.mainloop()

    def continue_startup(self):

        self.settings_save_manager = SettingsSaveManager(self)
        self.settings_save = {}
        for i in range(50):
            self.settings_save[str(i)] = "UNDEFINED"
        if len(self.settings_save_manager.list_saves()) < 1:
            self.settings_save_manager.fill_default_settings(self)
            self.settings_save_manager.save(self.settings_save)

        self.settings_save = self.settings_save_manager.load()
        self.settings_save_manager.check_values()

        if self.settings_save["2"] == "DARK":
            self.dark = True
            self.text_color = "#afb1b3"
            self.bg_color = "#2b2b2b"
            self.bg_select = "#3e3f41"
            self.highlight_color = "#d4d6d9"
        else:
            self.dark = False
            self.bg_color = "#f0f0f0"
            self.bg_select = "#D8E6F1"
            self.text_color = "#282828"
            self.highlight_color = "#0078D4"




        self.save_manager = SaveManager(self, self.settings_save["0"])
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


        self.splash_screen.text.config(text="Waiting for selection")
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
        self.settings_save_manager.save()
        raise SystemExit

    def exit_no_save(self):
        raise SystemExit

    def save_year(self):
        print("Saving...")
        self.save_manager.save(self.selected_year, self.save)
        self.settings_save_manager.save()


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
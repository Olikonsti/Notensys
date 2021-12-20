from tkinter import *
import tkinter.ttk as ttk
from Settings import *
from About import *

from WindowFeatures.SubjectOverview import *
from WindowFeatures.SubjectAttributes import *

class Window(Tk):
    def __init__(self, notensys):
        super().__init__()
        self.notensys = notensys
        self.title("Notensys Übersicht")
        self.geometry("600x500")
        #self.resizable(False, True)
        self.iconbitmap("DATA/icon.ico")
        self.settings_open = False
        self.settings_instance = None
        self.active_grade_editor = None


        self.menubar = Menu(self)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Speichern", command=self.notensys.save_year)
        filemenu.add_command(label="Speichern & Beenden", command=self.notensys.save_year_exit)
        self.menubar.add_cascade(label="Datei", menu=filemenu)
        self.menubar.add_cascade(label="Einstellungen", command=self.open_settings)
        self.menubar.add_cascade(label="Jahr ändern", command=self.change_year)
        self.menubar.add_cascade(label="Über Notensys", command=self.open_about)
        self.config(menu=self.menubar)

        self.update()
        self.notensys.window = self

        self.topbar = Frame(self)
        self.topbar.pack(fill=X)

        self.subject_overview = SubjectOverview(self, notensys)

        self.rightPane = Frame(self, width=300)
        self.rightPane.pack(side=RIGHT, fill=Y, padx=5, pady=(0, 5))

        self.subject_attributes = SubjectAttributes(self.rightPane, self.notensys)
        self.subject_attributes.pack(fill=BOTH, expand=True)

        self.bottom_right_pane = LabelFrame(self.rightPane, text="Leistungsnachweise", width=300, height=1000)
        self.bottom_right_pane.pack_propagate(False)
        self.bottom_right_pane.pack(fill=BOTH, expand=True)

        self.rechnung_erklaerung = LabelFrame(self.bottom_right_pane, text="Rechnung", height=100)
        self.rechnung_erklaerung.pack(padx=5, pady=(0, 5), side=BOTTOM, fill=X)
        self.text = Label(self.rechnung_erklaerung, text="(KL+GL)/2")
        self.text.pack()

        self.protocol("WM_DELETE_WINDOW", self.notensys.save_year_exit)

        self.update()

    def change_year(self):
        self.notensys.save_year()
        self.destroy()
        self.notensys.open_year_selector()

    def open_settings(self):
        Settings(self)
        self.settings_instance.grab_set()
        self.settings_instance.focus_force()

    def open_about(self):
        ab = About(self)
        ab.grab_set()
        ab.focus_force()





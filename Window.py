from Settings import *
from About import *
from tkdarktitle import *
from WindowFeatures.TitleBarMenuItem import *

from WindowFeatures.SubjectOverview import *
from WindowFeatures.SubjectAttributes import *
from BlurWindow import *

class Window(Tk):
    def __init__(self, notensys):
        super().__init__()
        self.notensys = notensys
        self.title("Notensys Übersicht")
        self.geometry("650x600")
        self.config(bg=self.notensys.bg_color_blur)

        if notensys.dark:
            dark_title_bar(self)
            self.blur_enabled = self.notensys.settings_save["3"]
            if self.blur_enabled:
                self.blur = BlurWindow(self, "#1c1c1c")
        else:
            self.blur_enabled = False
        #self.blur.enable()

        self.expanded = False

        self.style = ttk.Style(self)
        if self.notensys.dark:
            self.tk.call("source", "DATA/theme/sun-valley.tcl")
            self.tk.call("set_theme", "dark")
            if self.blur_enabled:
                self.enable_blur()

        else:
            self.tk.call("source", "DATA/theme/sun-valley.tcl")
            self.tk.call("set_theme", "light")


        #self.resizable(False, True)
        self.iconbitmap("DATA/icon.ico")
        self.settings_open = False
        self.settings_instance = None
        self.active_grade_editor = None

        self.menubar_frame = Frame(self, height=22)
        self.menubar_frame.pack_propagate(False)
        self.menubar_frame.pack(side=TOP, fill=X)

        self.file_menu_btn = TitleBarMenuItem(self.menubar_frame, notensys, "Datei")

        filemenu = Menu(self.file_menu_btn, tearoff=0)
        self.file_menu_btn["menu"] = filemenu
        filemenu.add_command(label="Speichern", command=self.notensys.save_year)
        filemenu.add_command(label="Speichern & Beenden", command=self.notensys.save_year_exit)
        filemenu.add_command(label="Ohne Speichern Beenden", command=self.notensys.exit_no_save)

        TitleBarItem(self.menubar_frame, notensys, "Einstellungen", self.open_settings)
        TitleBarItem(self.menubar_frame, notensys, "Jahr ändern", self.change_year)
        TitleBarItem(self.menubar_frame, notensys, "Über Notensys", self.open_about)

        self.update()
        self.notensys.window = self

        self.subject_overview = SubjectOverview(self, notensys)

        self.rightPane = Frame(self)
        self.rightPane.pack(side=RIGHT, fill=Y, padx=5, pady=(0, 5))

        self.subject_attributes = SubjectAttributes(self.rightPane, self.notensys)
        self.subject_attributes.pack(fill=BOTH, expand=True)

        self.bottom_right_pane = ttk.LabelFrame(self.rightPane, text="Leistungsnachweise", width=260, height=1000)
        self.bottom_right_pane.pack_propagate(False)
        self.bottom_right_pane.pack(fill=BOTH, expand=True)

        self.rechnung_erklaerung = ttk.LabelFrame(self.bottom_right_pane, text="Rechnung", height=100)
        self.rechnung_erklaerung.pack(padx=5, pady=(0, 5), side=BOTTOM, fill=X)
        self.text = Label(self.rechnung_erklaerung, text="(KL+GL)/2")
        self.text.pack()

        self.protocol("WM_DELETE_WINDOW", self.notensys.save_year_exit)

        self.update()

    def enable_blur(self):
        self.blur_enabled = True
        try:
            self.blur.enable()
        except:
            self.blur = BlurWindow(self, "#1c1c1c")
            self.blur.enable()

    def disable_blur(self):
        self.blur.disable()
        self.blur_enabled = False


    def change_geometry_width(self, pixels):
        try:
            width = self.winfo_width()
            height = self.winfo_height()
            self.bottom_right_pane.config(width=self.bottom_right_pane.winfo_width()+pixels)
            self.geometry(f"{width+pixels}x{height}")
        except:
            pass

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





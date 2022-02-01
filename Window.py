import tkinter.messagebox

from Settings import *
from About import *
from WindowFeatures.TitleBarMenuItem import *
from WindowFeatures.SubjectOverview import *
from WindowFeatures.SubjectAttributes import *
from WindowFeatures.HeadlineLabel import HeadlineLabel
from Utils.BlurEnabler import enable_blur

from Utils.KombifachCreator import *




class Window(Tk):
    def __init__(self, notensys):
        super().__init__()
        self.notensys = notensys
        self.title("Notensys Übersicht")
        self.geometry("650x680")
        self.config(bg=self.notensys.bg_color_blur)

        if notensys.dark:
            try:
                pass
                dark_title_bar(self)
            except:
                print("could not enable dark title bar on main win")
        self.blur_enabled = self.notensys.settings_save["3"]
        if self.blur_enabled:
            try:
                enable_blur(self, dark_mode=notensys.dark)
                print("blur enabled!!!")
            except:
                print("failed to start main win blur")

        self.expanded = False

        self.style = ttk.Style(self)
        if self.notensys.web_mode:
            self.tk.call("source", f"{notensys.DATA}/theme/sun-valley-web.tcl")
        else:
            self.tk.call("source", "DATA/theme/sun-valley.tcl")
        if self.notensys.dark:
            self.tk.call("set_theme", "dark")
        else:
            self.tk.call("set_theme", "light")
        try:
            self.iconbitmap("DATA/icon.ico")
        except:
            print("failed to load main win icon")
        self.settings_open = False
        self.settings_instance = None
        self.active_grade_editor = None

        self.menubar_frame = Frame(self, height=30)
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

        self.subj_menu_btn = TitleBarMenuItem(self.menubar_frame, notensys, "Kombi einrichten")

        subj_menu = Menu(self.subj_menu_btn, tearoff=0)
        self.subj_menu_btn["menu"] = subj_menu
        subj_menu.add_command(label="Geschichte/Sozi erstellen", command=self.open_kombifachcreator)

        self.update()
        self.notensys.window = self

        self.subject_overview = SubjectOverview(self, notensys)

        self.rightPane = Frame(self)
        self.rightPane.pack(side=RIGHT, fill=Y, padx=5, pady=(0, 5))

        self.subject_attributes = SubjectAttributes(self.rightPane, self.notensys)
        self.subject_attributes.pack(fill=BOTH, expand=True, padx=5, pady=(0, 5))

        self.bottom_right_pane = Frame(self.rightPane, width=270, height=1000)
        self.bottom_right_pane.pack_propagate(False)
        self.bottom_right_pane.pack(fill=BOTH, expand=True)

        self.protocol("WM_DELETE_WINDOW", self.notensys.save_year_exit)

        self.update()

    def disable_blur(self):
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

    def open_about(self):
         About(self)

    def open_kombifachcreator(self):
        already_kombi = False
        for i in self.notensys.save["grades"]:
            if "sk_gs_kombi" in self.notensys.save["grades"][i]["NBT"]:
                already_kombi = True
        if not already_kombi:
            KombifachCreator(self)
        else:
            tkinter.messagebox.showerror("Fehler beim Erstellen", "Kombi existiert schon")





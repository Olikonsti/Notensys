import tkinter.messagebox
from tkinter import *
import tkinter.ttk as ttk
from Utils.tkdarktitle import *

class YearSelector(Tk):
    def __init__(self, notensys):
        super().__init__()
        try:
            self.iconbitmap(f"{notensys.DATA}/icon.ico")
        except:
            print("could not load icon")
        if notensys.dark:
            self.config(bg="#1c1c1c")
            ui_load_label = Label(self, text="UI und Speicherdateien Laden...", bg="#1c1c1c", font="SegoeUI 14", fg="#F0F0F0")
            ui_load_label.pack(expand=True, padx=30, pady=30)
            self.update()
        self.notensys = notensys

        if notensys.dark:
            try:
                dark_title_bar(self)
            except:
                pass
            try:
                if self.notensys.web_mode:
                    self.tk.call("source", f"{notensys.DATA}/theme/sun-valley-web.tcl")
                else:
                    self.tk.call("source", f"{notensys.DATA}/theme/sun-valley.tcl")
                self.tk.call("set_theme", "dark")
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Theme Loading Error: {e}")
                raise SystemExit

        self.notensys = notensys
        self.title("Jahr wählen")
        self.geometry("300x100")
        #self.resizable(False, False)


        self.protocol("WM_DELETE_WINDOW", self.clean_exit)
        try:
            ui_load_label.config(text="Speicherdateien überprüfen...")
        except:
            pass


        self.years = self.notensys.save_manager.list_saves()
        self.option_var = StringVar(self)

        self.selector = ttk.OptionMenu(self, self.option_var, self.notensys.save_manager.get_last_modified(), *self.years)
        self.selector.pack(side=LEFT, padx=(20,0), pady=20)

        self.apply_btn = ttk.Button(self, text="Weiter", command=self.exit)
        self.apply_btn.pack(side=RIGHT, anchor=SW, padx=(5, 10), pady=(0, 10))

        self.open_folder_btn = ttk.Button(self, text="Ordner öffnen", command=self.notensys.save_manager.open_folder)
        self.open_folder_btn.pack(side=RIGHT, anchor=SW, padx=(10, 0), pady=(0, 10))

        try:
            ui_load_label.destroy()
        except:
            pass

        self.geometry("300x100")

        self.mainloop()

    def exit(self):
        try:
            self.notensys.splash_screen.destroy()
        except:
            pass
        self.destroy()

    def clean_exit(self):
        raise SystemExit

    def get_selection(self):
        return self.option_var.get()
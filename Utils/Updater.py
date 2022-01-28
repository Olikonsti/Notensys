import os
import time
import tkinter.messagebox
from tkinter import *
import requests
import tkinter.ttk as ttk
from BlurWindow.blurWindow import GlobalBlur
import ctypes as ct
from Utils.tkdarktitle import dark_title_bar
from Utils.VerticalScrolledFrame import VerticalScrolledFrame
from Utils.BlurEnabler import enable_blur

class Updater(Tk):
    def __init__(self, notensys):
        super().__init__()
        self.notensys = notensys
        self.open = True
        self.resizable(False, False)

        self.check_update()

        if self.open:
            self.load_gui()
        else:
            self.exit()



    def display_info(self, text):
        a = Tk()
        a.title("Notensys updater")
        a.geometry("500x200")
        a.config(bg="#1c1c1c")

        try:
            dark_title_bar(a)

            get_parent = ct.windll.user32.GetParent
            hwnd = get_parent(a.winfo_id())
            GlobalBlur(hwnd, hexColor="#030202", Dark=True, Acrylic=True)
            self.blur_enabled = True
        except:
            pass



        Label(a, text=text, font="SegoeUI 14", bg="#1c1c1c", fg="#ffffff").pack(expand=True, padx=10)

        return a

    def load_gui(self):
        notensys = self.notensys

        self.protocol("WM_DELETE_WINDOW", self.exit)

        color = "#1c1c1c"
        self.config(bg=color)
        try:
            self.iconbitmap(f"{notensys.DATA}/icon.ico")
        except:
            print("could not load icon")
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

        try:
            enable_blur(self)
        except:
            print("BLUR UPDATER ERROR")


        self.notensys = notensys
        self.title("Notensys Updater")
        self.geometry("600x600")

        us = Label(self, text="Update verfügbar", font="SegoeUI 22")
        us.pack(side=TOP, anchor=NW, padx=20, pady=10)

        test = Label(self, text=f"""
Notensys hat ein neues Update bekommen.
Deine aktuelle Version: {notensys.version}
Die neuste Version {self.newest_version}
        """, font="SegoeUIVariable 14", justify=LEFT)
        test.pack(side=TOP, anchor=NW, padx=20, pady=10)

        label_f = ttk.LabelFrame(self, text="Änderungen in der neusten Version")
        label_f.pack(side=TOP, anchor=NW, padx=20, pady=10, expand=True, fill=BOTH)

        scf = VerticalScrolledFrame(label_f)
        scf.pack(expand=True, fill=BOTH)
        text = Label(scf.interior, justify=LEFT, text=self.changelog, font="Helvetica 11", wraplengt=500)
        text.pack(side=TOP, anchor=NW, padx=10, pady=10)

        btm_frame = ttk.Frame(self)
        btm_frame.pack(side=BOTTOM, fill=X)
        self.install_btn = ttk.Button(btm_frame, text="installieren", command=self.download, style="Accent.TButton")
        self.install_btn.pack(side=RIGHT, padx=10, pady=10)
        self.install_btn = ttk.Button(btm_frame, text="Nicht installieren", command=self.exit)
        self.install_btn.pack(side=RIGHT, padx=0, pady=10)

        if self.open:
            while self.open:
                self.update()
        else:
            self.exit()

    def exit(self):
        self.open = False
        try:
            self.destroy()
        except:
            pass

    def check_update(self):
        # AUTO UPDATE
        try:
            response = requests.get("https://api.github.com/repos/Olikonsti/Notensys/releases/latest")
            print(response.json())
            self.changelog = response.json()["body"]
            newest_version = response.json()["tag_name"]
            self.newest_version = newest_version
            print(newest_version)

            if float(newest_version) > float(self.notensys.version):
                pass
            else:
                self.exit()
        except Exception as e:
            print(f"ERROR FETCHING UPDATES: {e}")
            self.exit()

    def download(self):
        url = f'https://github.com/Olikonsti/Notensys/releases/download/{self.newest_version}/NotensysInstaller_{self.newest_version}.exe'
        d = self.display_info("Version wird heruntergeladen. \nDas Programm wird sich kurz aufhängen!")
        d.update()
        r = requests.get(url, allow_redirects=True)
        open('../NS_update.exe', 'wb').write(r.content)
        os.system("start NS_update.exe")
        # self.open_download(newest_version)
        print("sys exit")
        os.system("taskkill /F /IM notensys.exe")
        raise SystemExit
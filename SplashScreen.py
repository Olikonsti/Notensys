import time
import tkinter.messagebox
from tkinter import *
import tkinter.ttk as ttk
import requests
import webbrowser

class SplashScreen(Tk):
    def __init__(self, notensys):
        super().__init__()

        self.overrideredirect(True)
        self.notensys = notensys

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.geometry(f"600x300+{int(screen_width/2)-300}+{int(screen_height/2)-150}")

        self.text = Label(self, text="Notensys", font="System 30")
        self.text.pack(pady=10)

        self.text = Label(self, text=f"Version {self.notensys.version}", font="System 20")
        self.text.pack(pady=10)

        self.text = Label(self, text="Coded by Konstantin Ehmann", font="System 20")
        self.text.pack(pady=10)

        self.text = Label(self, text="Checking for Updates...", font="System 30")
        self.text.pack(pady=10)

        self.bar = ttk.Progressbar(self, orient=HORIZONTAL, mode="indeterminate", length=280, maximum=15)
        self.bar.pack(fill=X, padx=10)
        self.bar.start(70)

        self.update()

        # AUTO UPDATE
        try:
            response = requests.get("https://api.github.com/repos/Olikonsti/Notensys/releases/latest")
            newest_version = response.json()["tag_name"]
            if float(newest_version) > float(notensys.version):
                result = tkinter.messagebox.askquestion("Notensys Updater",
                                                        f"Eine neue Version von Notensys ist verfügbar!\nDeine Version: {self.notensys.version}\nNeuste Version: {newest_version}\nDrücke ja zum öffnen der Download Seite")
            else:
                result = "no"
        except:
            print("ERROR FETCHING UPDATES ")
            result = "no"

        if result == "yes":
            self.open_download(newest_version)
            raise SystemExit


        self.after(500, self.exit)

        self.mainloop()

    def open_download(self, tag):
        webbrowser.open(f"https://github.com/Olikonsti/Notensys/releases/tag/{tag}")

    def ready(self):
        self.bind("<Key>", self.exit)
        self.bind("<Button-1>", self.exit)
        self.bar.destroy()
        self.text.config(text="Press Any Key")

    def exit(self, e=None):
        self.destroy()
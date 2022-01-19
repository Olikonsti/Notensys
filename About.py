from tkinter import *
import tkinter.ttk as ttk
from BlurWindow import *
from PIL import Image, ImageTk
import webbrowser
from tkdarktitle import *


class About(Toplevel):
    def __init__(self, window):
        super().__init__(window)
        self.window = window

        self.tImg = Image.open('DATA/icon.ico')
        self.img = ImageTk.PhotoImage(self.tImg)

        if self.window.blur_enabled:
            self.window.blur.block_lift()




        self.resizable(False, False)
        if window.notensys.dark:
            dark_title_bar(self)

        self.iconbitmap("DATA/icon.ico")
        self.title("Über Notensys")
        self.geometry("300x400")



        self.protocol("WM_DELETE_WINDOW", self.exit)
        panel = Label(self, image=self.img)
        panel.photo = self.img
        panel.pack()

        if window.notensys.dark:
            self.config(bg="#1c1c1c")
            if window.blur_enabled:
                self.blur = BlurWindow(self, "#1c1c1c")
                self.blur.enable()

        if window.blur_enabled:
            self.after(2, self.blur.lift_bg())

        self.bind("<FocusOut>", self.blur.lift_bg)

        self.bind("<FocusIn>", lambda e: (self.blur.lift_bg(), print("FOC")))


        Label(self, text=f"Version: {self.window.notensys.version}").pack()
        Label(self, text=f"Datum: {self.window.notensys.version_date}").pack()
        Label(self, text=f"Programmiert von: Konstantin Ehmann").pack()

        link1 = Label(self, text="Notensys Github Seite", fg="#61afef", cursor="hand2", bg=self.window.notensys.bg_color)
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://github.com/Olikonsti/Notensys"))

        Label(self, text=f"Danke für die Benutzung von Notensys!").pack()
        Label(self, text=f"Fehler und Verbesserungsvorschläge\nkannst du hier melden:").pack()

        link1 = Label(self, text="Notensys Github issues", fg="#61afef", cursor="hand2", bg=self.window.notensys.bg_color)
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://github.com/Olikonsti/Notensys/issues"))

        link1 = Label(self, text="Tkinter Theme", fg="#61afef", cursor="hand2",
                      bg=self.window.notensys.bg_color)
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://github.com/rdbende/Sun-Valley-ttk-theme"))

        def callback(url):
            webbrowser.open_new(url)


    def exit(self):
        if self.window.blur_enabled:
            self.window.blur.unblock_lift()
        self.destroy()

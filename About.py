import time
from tkinter import *
import tkinter.ttk as ttk
from WindowFeatures.HeadlineLabel import *
from PIL import Image, ImageTk
import webbrowser
from Utils.tkdarktitle import *
from Utils.BlurEnabler import enable_blur



class About(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window

        #self.grab_set()
        #self.focus_force()

        self.tImg = Image.open('DATA/icon.ico')
        self.img = ImageTk.PhotoImage(self.tImg)

        top = Frame(self)
        top.pack(fill=X)

        self.back_btn = ttk.Button(top, text="<", command=self.exit)
        self.back_btn.pack(padx=10, pady=10, side=LEFT)

        self.headline = HeadlineLabel(top, text="Über Notensys")
        self.headline.pack(side=LEFT)

        self.inner = Frame(self)
        self.inner.pack(expand=True)

        #self.iconbitmap("DATA/icon.ico")
        #self.title("Über Notensys")
        #self.geometry("300x400")

        #self.protocol("WM_DELETE_WINDOW", self.exit)
        panel = Label(self.inner, image=self.img)
        panel.photo = self.img
        panel.pack()

        if window.notensys.dark:
            self.config(bg="#1c1c1c")
            if window.blur_enabled:
                try:
                    enable_blur(self)
                except:
                    pass


        Label(self.inner, text=f"Version: {self.window.notensys.version}").pack()
        Label(self.inner, text=f"Datum: {self.window.notensys.version_date}").pack()
        Label(self.inner, text=f"Programmiert von: Konstantin Ehmann").pack()

        link1 = Label(self.inner, text="Notensys Github Seite", fg="#61afef", cursor="hand2", bg=self.window.notensys.bg_color)
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://github.com/Olikonsti/Notensys"))

        Label(self.inner, text=f"Danke für die Benutzung von Notensys!").pack()
        Label(self.inner, text=f"Fehler und Verbesserungsvorschläge\nkannst du hier melden:").pack()

        link1 = Label(self.inner, text="Notensys Github issues", fg="#61afef", cursor="hand2", bg=self.window.notensys.bg_color)
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://github.com/Olikonsti/Notensys/issues"))

        link1 = Label(self.inner, text="Tkinter Theme", fg="#61afef", cursor="hand2",
                      bg=self.window.notensys.bg_color)
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://github.com/rdbende/Sun-Valley-ttk-theme"))

        def callback(url):
            webbrowser.open_new(url)

        self.config(width=self.window.winfo_width(), height=self.window.winfo_height())
        self.pack_propagate(False)
        self.place(x=0, y=0)

        self.upd()

    def upd(self):
        self.config(width=self.window.winfo_width(), height=self.window.winfo_height())
        self.after(100, self.upd)

    def exit(self):
        self.destroy()

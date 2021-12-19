from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import webbrowser


class About(Toplevel):
    def __init__(self, window):
        super().__init__(window)

        self.iconbitmap("DATA/icon.ico")
        self.title("Über Notensys")
        self.geometry("300x400")
        self.resizable(False, False)

        self.window = window

        self.protocol("WM_DELETE_WINDOW", self.exit)
        self.tImg = Image.open('DATA/icon.ico')
        self.img = ImageTk.PhotoImage(self.tImg)
        panel = Label(self, image=self.img)
        panel.photo = self.img
        panel.pack()

        Label(self, text=f"Version: {self.window.notensys.version}").pack()
        Label(self, text=f"Datum: {self.window.notensys.version_date}").pack()
        Label(self, text=f"Programmiert von: Konstantin Ehmann").pack()

        link1 = Label(self, text="Notensys Github Seite", fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://github.com/Olikonsti/Notensys"))

        Label(self, text=f"Danke für die Benutzung von Notensys!").pack()
        Label(self, text=f"Fehler und Verbesserungsvorschläge\nkannst du hier melden:").pack()

        link1 = Label(self, text="Notensys Github issues", fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://github.com/Olikonsti/Notensys/issues"))

        def callback(url):
            webbrowser.open_new(url)


    def exit(self):
        self.destroy()

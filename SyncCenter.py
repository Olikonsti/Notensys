import time
from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from Utils.tkdarktitle import *
from Utils.BlurEnabler import enable_blur


class SyncCenter(Toplevel):
    def __init__(self, window):
        super().__init__(window)
        self.window = window

        self.grab_set()
        self.focus_force()

        self.tImg = Image.open('DATA/icon.ico')
        self.img = ImageTk.PhotoImage(self.tImg)

        self.resizable(False, False)
        if window.notensys.dark:
            try:
                dark_title_bar(self)
            except:
                pass

        self.iconbitmap("DATA/icon.ico")
        self.title("Synchronisierung")
        self.geometry("400x300")

        self.protocol("WM_DELETE_WINDOW", self.exit)
        panel = Label(self, image=self.img)
        panel.photo = self.img
        panel.pack()

        if window.notensys.dark:
            self.config(bg="#1c1c1c")
            if window.blur_enabled:
                try:
                    enable_blur(self)
                except:
                    pass

    def exit(self):
        self.destroy()

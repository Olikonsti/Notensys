from tkinter import *
import tkinter.ttk as ttk


class Settings(Toplevel):
    def __init__(self, window):
        super().__init__(window)

        self.iconbitmap("DATA/icon.ico")
        self.title("Notensys Einstellungen")
        self.geometry("500x500")

        self.window = window
        self.window.settings_open = True
        self.window.settings_instance = self

        self.protocol("WM_DELETE_WINDOW", self.exit)

    def exit(self):
        self.destroy()
        self.window.settings_open = False

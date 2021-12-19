from tkinter import *
import tkinter.ttk as ttk

class ColorIndicator(Frame):
    def __init__(self, parent, points):
        super().__init__(parent, width=40, height=17)

        try:
            if points < 1:
                self.config(bg="#ad0000")
            elif points < 4:
                self.config(bg="#ff4d00")
            elif points < 7:
                self.config(bg="#ff8c00")
            elif points < 10:
                self.config(bg="#e6dd32")
            elif points < 13:
                self.config(bg="#abf740")
            else:
                self.config(bg="#00bf03")
        except:
            self.config(bg="grey")




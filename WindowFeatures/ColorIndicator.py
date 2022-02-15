from tkinter import *
import tkinter.ttk as ttk

class ColorIndicator(Frame):
    def __init__(self, parent, points):
        super().__init__(parent, width=40, height=17)

        try:
            if points < 1:
                self.config(bg="#ad0000")
            elif points < 3.5:
                self.config(bg="#ff4d00")
            elif points < 6.5:
                self.config(bg="#ff8c00")
            elif points < 9.5:
                self.config(bg="#e6dd32")
            elif points < 12.5:
                self.config(bg="#9beb23")
            else:
                self.config(bg="#289100")
        except:
            self.config(bg="grey")




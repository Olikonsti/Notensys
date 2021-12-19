from tkinter import *
import tkinter.ttk as ttk

class SplashScreen(Tk):
    def __init__(self, notensys):
        super().__init__()

        self.overrideredirect(True)
        self.notensys = notensys

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.geometry(f"400x300+{int(screen_width/2)-200}+{int(screen_height/2)-150}")


        self.text = Label(self, text="Notensys", font="System 30")
        self.text.pack(pady=10)

        self.text = Label(self, text=f"Version {self.notensys.version}", font="System 20")
        self.text.pack(pady=10)

        self.text = Label(self, text="Coded by Konstantin Ehmann", font="System 20")
        self.text.pack(pady=10)

        self.text = Label(self, text="Loading...", font="System 30")
        self.text.pack(pady=10)

        self.bar = ttk.Progressbar(self, orient=HORIZONTAL, mode="indeterminate", length=280, maximum=15)
        self.bar.pack(fill=X, padx=10)
        self.bar.start(70)



        self.after(500, self.ready)

        self.mainloop()

    def ready(self):
        self.bind("<Key>", self.exit)
        self.bind("<Button-1>", self.exit)
        self.bar.destroy()
        self.text.config(text="Press Any Key")

    def exit(self, e=None):
        self.destroy()
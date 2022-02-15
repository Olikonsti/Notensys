from tkinter import *
import tkinter.ttk as ttk

class Popup(Frame):
    def __init__(self, window, text, time=5):
        super().__init__(window)
        try:
            window.COUNT_POPUPS
        except:
            window.COUNT_POPUPS = 0
        window.COUNT_POPUPS += 1
        self.window = window
        self.progress_count = 0
        self.width = 350
        self.x_pos = -600
        self.start_slide_speed = 10
        self.slide_speed = self.start_slide_speed
        self.tick_time = time

        self.y_pos = 690 - 105*window.COUNT_POPUPS - 12

        self.config(width=self.width, height=80, highlightthickness=1, highlightbackground=window.notensys.highlight_color_selected, highlightcolor=window.notensys.highlight_color_selected, bg=window.notensys.bg_select)
        self.pack_propagate(False)
        self.lift()

        self.place(y=self.y_pos, x=10)

        self.progress = Frame(self, width=self.width)
        self.progress.pack(anchor=NW)

        self.progress_inner = Frame(self.progress, width=0, height=4, bg="#1b713c")
        self.progress_inner.pack(side=LEFT)

        self.message = Label(self, text=text, bg=window.notensys.bg_select, justify=LEFT, wraplength=self.width - 10)
        self.message.pack(anchor=NW, padx=6, pady=6)

        close_btn = Label(self, text="X", bg=self.window.notensys.bg_select)
        close_btn.place(x=self.width - 30, y=10)
        close_btn.bind("<Button-1>", self.slideout)

        self.slidein()

    def slidein(self):
        if self.x_pos < 12:
            self.lift()
            self.place(x=self.x_pos, y=self.y_pos)
            self.x_pos += self.slide_speed
            self.slide_speed -= 0.01
            self.window.after(5, self.slidein)
        else:
            self.increase_progress()

    def slideout(self, event=None):
        if self.x_pos > -600:
            self.place(x=int(self.x_pos), y=self.y_pos)
            self.slide_speed += 0.1
            self.x_pos -= self.slide_speed

            self.window.after(5, self.slideout)
        else:
            self.window.COUNT_POPUPS -= 1

    def increase_progress(self):
        if self.progress_count < 100:
            self.lift()
            self.progress_count += 0.2
            self.progress_inner.config(width=(self.progress_count/100)*self.progress["width"])
            self.window.after(self.tick_time, self.increase_progress)
        else:
            self.slideout()
            print("sl")

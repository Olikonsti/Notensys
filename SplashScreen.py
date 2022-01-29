import webbrowser
from Utils.Updater import *

class SplashScreen(Tk):
    def __init__(self, notensys):
        super().__init__()
        self.notensys = notensys
        self.overrideredirect(True)
        color = "#1c1c1c"
        self.config(bg=color)
        try:
            dark_title_bar(self)

            get_parent = ct.windll.user32.GetParent
            hwnd = get_parent(self.winfo_id())
            GlobalBlur(hwnd, hexColor="#030202", Dark=True, Acrylic=True)
            self.blur_enabled = True
        except:
            pass

        #self.overrideredirect(True)
        frameCnt = 18
        frames = [PhotoImage(file='DATA/loading.gif', format='gif -index %i' % (i)) for i in range(2, frameCnt)]


        def update(ind):
            frame = frames[ind]
            ind += 1
            if ind == frameCnt-2:
                ind = 1
            #label.configure(image=frame)
            #label.create_image( 100, 100, image=frame)
            label.configure(image=frame)
            self.after(60, update, ind)

        label = Label(self, width=100, height=100, bg=color)

        label.pack(expand=True, fill=BOTH)
        self.after(1, update, 0)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.config(bg=color)

        self.geometry(f"600x400+{int(screen_width/2)-300}+{int(screen_height/2)-150}")

        self.text = Label(self, text="Notensys", font="SegoeUI 30", bg=color, fg="#afb1b3")
        self.text.pack(pady=10)

        self.text = Label(self, text=f"Version {self.notensys.version}", font="SegoeUI 20", fg="#afb1b3", bg=color)
        self.text.pack(pady=10)

        self.text = Label(self, text="Coded by Konstantin Ehmann", font="SegoeUI 20", fg="#afb1b3", bg=color)
        self.text.pack(pady=10)

        self.text = Label(self, text="Checking for Updates...", font="SegoeUI 30", fg="#afb1b3", bg=color)
        self.text.pack(pady=10)

        self.update()

        Updater(self.notensys)


        self.after(1, self.exit)



    def open_download(self, tag):
        webbrowser.open(f"https://github.com/Olikonsti/Notensys/releases/tag/{tag}")

    def ready(self):
        self.bind("<Key>", self.exit)
        self.bind("<Button-1>", self.exit)
        self.bar.destroy()
        self.text.config(text="Press Any Key")

    def exit(self, e=None):
        self.notensys.continue_startup()

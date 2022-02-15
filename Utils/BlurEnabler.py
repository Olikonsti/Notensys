import ctypes as ct
import time
from BlurWindow.blurWindow import *

def enable_blur(win, dark_mode=True):

    global DRAG
    get_parent = ct.windll.user32.GetParent
    HWND = get_parent(win.winfo_id())

    color = "#03020233"

    DRAG = False

    def dragging(event):
        global DRAG
        if event.widget is win:  # if is event Configure of root (Drag,Resize)
            time.sleep(0.01) # reduce lag on win 10
            if DRAG == False:  # If Drag is disabled (set by stop_drag)
                pass
                # GlobalBlur(HWND, Acrylic=False)
            else:
                win.after_cancel(DRAG)  # cancel task \/ (is dragging)
            DRAG = win.after(200, stop_drag)  # execute stop_drag after 200ms

    def stop_drag():
        global DRAG
        DRAG = False

        if not dark_mode:
            pass
        else:
            GlobalBlur(HWND, hexColor=color, Dark=True, Acrylic=True)


    win.bind('<Configure>', dragging)
    if not dark_mode:
        print("blur enabler enabled!")
    else:
        GlobalBlur(HWND, hexColor=color, Dark=True, Acrylic=True)
    win.blur_enabled = True
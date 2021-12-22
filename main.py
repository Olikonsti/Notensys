from Notensys import *

DEBUG = True

if DEBUG:
    Notensys()
else:
    try:
        Notensys()
    except Exception as e:
        tkinter.messagebox.showerror(f"Notensys Programm fataler Fehler", f"Bitte Melde diesen Fehler dem Ersteller des Programms!\nWichtiger traceback:{e}\nMeldemöglichkeit: https://github.com/Olikonsti/Notensys/issues\nEin Löschen der Settingsdatei kann auch helfen")
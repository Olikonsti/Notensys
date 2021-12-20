import os
import tkinter.messagebox
import json


class SaveManager():
    def __init__(self, notensys, savefolder):
        self.notensys = notensys
        self.savefolder = savefolder

    def save(self, name, data):
        f = open(f"{self.savefolder}/{name}", "w")
        f.write(str(json.dumps(data, indent=4)))
        f.close()

    def load(self, name):
        f = open(f"{self.savefolder}/{name}", "r")
        data = f.read()
        f.close()
        try:
            exec(f"global out_; out_ = {data}")
        except Exception as e:
            tkinter.messagebox.showerror("Jahr laden: Fehler", f"Diese Datei is beschädigt und konnte nicht geladen werden.\nFEHLER:{e}")

        return out_

    def open_folder(self):
        os.startfile(self.savefolder)

    def list_saves(self):
        return os.listdir(self.savefolder)
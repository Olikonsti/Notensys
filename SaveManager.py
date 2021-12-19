import os
import tkinter.messagebox
import json

DATA_FOLDER = "DATA\Saves"

class SaveManager():
    def __init__(self, notensys):
        self.notensys = notensys

    def save(self, name, data):
        f = open(f"{DATA_FOLDER}/{name}", "w")
        f.write(str(json.dumps(data, indent=4)))
        f.close()

    def load(self, name):
        f = open(f"{DATA_FOLDER}/{name}", "r")
        data = f.read()
        f.close()
        try:
            exec(f"global out_; out_ = {data}")
        except Exception as e:
            tkinter.messagebox.showerror("Jahr laden: Fehler", f"Diese Datei is beschädigt und konnte nicht geladen werden.\nFEHLER:{e}")

        return out_

    def open_folder(self):
        os.startfile(DATA_FOLDER)

    def list_saves(self):
        return os.listdir(DATA_FOLDER)
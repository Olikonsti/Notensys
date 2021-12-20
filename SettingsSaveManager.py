import os
import tkinter.messagebox
import json
from Settings import *

DATA_FOLDER = "DATA\Settings"

class SettingsSaveManager():
    def __init__(self, notensys):
        self.notensys = notensys

    def save(self, data):
        f = open(f"{DATA_FOLDER}/settings.txt", "w")
        f.write(str(json.dumps(data, indent=4)))
        f.close()

    def fill_default_settings(self, notensys):
        Settings.fill_default_settings(0, notensys)

    def check_values(self):
        Settings.check_values(0, self.notensys)

    def load(self):
        global true, false;
        true = True
        false = False
        f = open(f"{DATA_FOLDER}/settings.txt", "r")
        data = f.read()
        f.close()
        try:
            exec(f"global out_; out_ = {data}")
        except Exception as e:
            tkinter.messagebox.showerror("Einstellungen laden: Fehler", f"Die Speicherdatei der Einstellungen is beschädigt und konnte nicht geladen werden.\nFEHLER:{e}")

        return out_

    def open_folder(self):
        os.startfile(DATA_FOLDER)

    def list_saves(self):
        return os.listdir(DATA_FOLDER)
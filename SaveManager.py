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

    def get_last_modified(self):
        folder = self.list_saves()
        biggest = folder[0]
        biggest_time = os.path.getmtime(self.savefolder + "/" + biggest)
        for i in folder:
            if os.path.getmtime(self.savefolder + "/" + i) > biggest_time:
                biggest = i
        return biggest

    def load(self, name):
        f = open(f"{self.savefolder}/{name}", "r")
        data = f.read()
        f.close()
        try:
            true = True
            false = False
            exec(f"global out_; out_ = {data}")

        except Exception as e:
            tkinter.messagebox.showerror("Jahr laden: Fehler", f"Diese Datei is beschädigt und konnte nicht geladen werden.\nFEHLER:{e}")
            raise SystemExit
        out = self.check_values(out_)
        return out

    def check_values(self, data):

        # add NBT tab for version 3.5
        for subject in data["grades"]:
            if "NBT" not in data["grades"][subject]:
                data["grades"][subject]["NBT"] = {}
            #if subject == "Geschichte":
                #data["grades"][subject]["NBT"]["ist_geschichte"] = True

        return data


    def open_folder(self):
        os.startfile(self.savefolder)

    def list_saves(self):
        try:
            return os.listdir(self.savefolder)
        except Exception as e:
            tkinter.messagebox.showerror("Error", str(e))
            raise SystemExit
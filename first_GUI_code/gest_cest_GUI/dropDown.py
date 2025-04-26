#Version 0.1.1 26/04/2025

from tkinter import messagebox
from tkinter.ttk import Combobox

class DropDown:
    def __init__(self, master, values, callback):
        self.combobox = Combobox(master, width=40)
        self.combobox["values"] = values
        self.combobox["state"] = "readonly"
        self.callback = callback

        if self.callback:
            self.combobox.bind("<<ComboboxSelected>>", self.callback)

    def getBasket(self):
        return self.combobox.get()
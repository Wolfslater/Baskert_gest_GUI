#Version 0.2.2 06/05/2025

from tkinter import Label, Button, Entry, messagebox
from tkinter.ttk import Combobox
from Cestino import Cestino 

class DropDown:
    def __init__(self, master, VALUES, callback):
        self.combobox = Combobox(master, width=40)
        self.combobox["values"] = VALUES
        self.combobox["state"] = "readonly"
        self.callback = callback

        if self.callback:
            self.combobox.bind("<<ComboboxSelected>>", self.callback)

    def getBasket(self):
        return self.combobox.get()

class Factory:

    @staticmethod
    def newLabel(master, text=None):
        label = Label(master, text=text)
        return label
    
    @staticmethod
    def newEntry(master, width=0):
        entry = Entry(master, width=width)
        return entry
    
    @staticmethod
    def newButton(master, text=None, command=None):
        button = Button(master, text=text, command=command)
        return button

    @staticmethod
    def gridConfig(widget, row, column, padx=0, pady=0, sticky="", columnspan=1):
        widget.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky, columnspan=columnspan)
        return widget

class Warning:
    def __init__(self, message):
        self.message = message

    def matchMessage(self):
        match self.message:
            case "1":
                return "Please select a basket first"
            case "2":
                return "ERROR: " \
                "MISSING DATA OR WRONG DATA TYPE." \
                "\nPrice and weight must be numeric values."

    def showWarning(self):
        messagebox.showwarning("WARNING", self.matchMessage())

class Baskets:
    def __init__(self):
        self.baskets = {
            "Basket 1": Cestino(),
            "Basket 2": Cestino(),
            "Basket 3": Cestino(),
            "Basket 4": Cestino(),
            "Basket 5": Cestino()
        }
    
    def addFruit(self, basketName, fruit):
        if basketName in self.baskets:
            self.baskets[basketName].add(fruit)

    def getBasket(self, basketName):
        if basketName in self.baskets:
            return self.baskets[basketName]
        else:
            return Warning("1").showWarning()
    
    def getBasketsName(self):
        return list(self.baskets.keys())
    
baskets = Baskets()
VALUES = baskets.getBasketsName()

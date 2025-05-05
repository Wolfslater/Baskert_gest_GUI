#Version 0.1.1 05/05/2025

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


basket_1 = Cestino()  # First basket instance
basket_2 = Cestino()  # Second basket instance
basket_3 = Cestino()  # Third basket instance
basket_4 = Cestino()  # Fourth basket instance
basket_5 = Cestino()  # Fifth basket instance
VALUES = ["Basket 1", "Basket 2", "Basket 3", "Basket 4", "Basket 5"]
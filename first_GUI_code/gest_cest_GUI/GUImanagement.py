# Version 0.3.3 21/04/2025

from addFruit import Button, Frutto, addFruit
from basketManager import BasketInfos
from tkinter import Toplevel

class GUIManagement:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x600")  # Set window size
        self.master.title("Gestionale GUI cestini di frutta")  # Set title

        # Buttons with commands
        self.addBtn = Button(self.master, text="Add fruit to the basket.", command=self.add)
        self.exitBtn = Button(self.master, text="Exit the the program.", command=self.exit)
        self.basketBtn = Button(self.master, text="Open basket manager", command=self.basketManager)

        # Layout
        self.addBtn.grid(row=0, column=0, padx=50)
        self.exitBtn.grid(row=0, column=1, padx=15)
        self.basketBtn.grid(row=0, column=2, padx=50)

        self.fruit = Frutto()  # Initialize fruit object

    def add(self):  # Open add fruit window
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        addFruit(self.newWindow, self.master, self.fruit)

    def exit(self):  # Exit program
        exit()

    def basketManager(self):  # Open basket manager
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        BasketInfos(self.newWindow, self.master)
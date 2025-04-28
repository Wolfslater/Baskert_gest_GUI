# Version 0.3.6 28/04/2925

from Frutto import Frutto
from addFruit import addFruit
from factory import Factory
from basketManager import BasketInfos
from tkinter import Toplevel

class GUIManagement:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x200")  # Set window size
        self.master.title("Main page")  # Set title
        self.fruit = Frutto()  # Initialize fruit object
        self.button = Factory.newButton
        self.grid = Factory.gridConfig

        # Buttons with commands
        self.addBtn = self.button(self.master, text="Add fruit to the basket.", command=self.add)
        self.exitBtn = self.button(self.master, text="Exit the the program.", command=self.exit)
        self.basketBtn = self.button(self.master, text="Open basket manager", command=self.basketManager)

        # Layout
        self.grid(widget=self.addBtn, row=0, column=0, padx=50)
        self.grid(widget=self.exitBtn, row=0, column=1, padx=15)
        self.grid(widget=self.basketBtn, row=0, column=2, padx=50)

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

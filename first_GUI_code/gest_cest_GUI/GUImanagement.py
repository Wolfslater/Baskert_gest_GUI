# Version 0.3.5 26/04/2925

from addFruit import Frutto, addFruit
from factory import Factory
from basketManager import BasketInfos
from tkinter import Toplevel

class GUIManagement:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x200")  # Set window size
        self.master.title("Main page")  # Set title

        # Buttons with commands
        self.addBtn = Factory.newButton(self.master, text="Add fruit to the basket.", command=self.add)
        self.exitBtn = Factory.newButton(self.master, text="Exit the the program.", command=self.exit)
        self.basketBtn = Factory.newButton(self.master, text="Open basket manager", command=self.basketManager)

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
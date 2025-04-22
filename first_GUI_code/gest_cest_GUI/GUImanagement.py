#Version 0.3.3 21/04/2925

from addFruit import Button, Frutto, addFruit
from basketManager import BasketInfos
from tkinter import Toplevel
from baskets import (basket_1, basket_2, 
                     basket_3, basket_4, basket_5)

class GUIManagement:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x600")
        self.master.title("Gestionale GUI cestini di frutta")

        self.addBtn = Button(self.master, text="Add fruit to the basket.", command=self.add)
        self.exitBtn = Button(self.master, text="Exit the the program.", command=self.exit)
        self.basketBtn = Button(self.master, text="Open basket manager", command=self.basketManager)

        self.addBtn.grid(row=0, column=0, padx=50, pady=0)
        self.exitBtn.grid(row=0, column=1, padx=15, pady=0)
        self.basketBtn.grid(row=0, column=2, padx=50, pady=0)

        self.fruit = Frutto()

    def add(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        addFruit(self.newWindow, self.master, self.fruit)

    def exit(self):
        exit()

    def basketManager(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        BasketInfos(self.newWindow, self.master)

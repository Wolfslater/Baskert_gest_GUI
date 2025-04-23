# Version 1.5.13 22/04/2025

from tkinter import Text
from addFruit import Combobox, Button, Label, END
from baskets import (basket_1, basket_2, 
                     basket_3, basket_4, basket_5)

class BasketInfos:
    def __init__(self, master, relative):
        # Initialize the GUI components
        self.master = master
        self.relative = relative
        self.selected_basket = ""

        # Labels and text area for basket details
        self.tare_label = Label()
        self.nett_label = Label()
        self.prize_label = Label()
        self.basket_content = Text(self.master)

        # Buttons for actions
        self.backBtn = Button(self.master, text="Back", command=self.back)
        self.tareBtn = Button(self.master, text="Disply tare", command=self.displayTare)
        self.nettBtn = Button(self.master, text="Disply nett", command=self.displayNett)
        self.basketBtn = Button(self.master, text="Disply basket", command=self.displayBasket)
        self.PrizetBtn = Button(self.master, text="Disply basket's prize", command=self.displayPrice)

        # Dropdown to select a basket
        self.combobox = Combobox(self.master, width=40)
        self.combobox["values"] = ["Basket 1", "Basket 2", "Basket 3", "Basket 4", "Basket 5"]
        self.combobox["state"] = "readonly"
        self.combobox.bind("<<ComboboxSelected>>", self.getChoice)

        # Arrange GUI components in a grid
        self.combobox.grid(row=0, column=5)
        self.backBtn.grid(row=0, column=0)
        self.tareBtn.grid(row=0, column=1)
        self.nettBtn.grid(row=0, column=2)
        self.basketBtn.grid(row=0, column=3)
        self.PrizetBtn.grid(row=0, column=4)

    def back(self):
        # Go back to the previous window
        self.relative.deiconify()
        self.master.destroy()

    def displayTare(self):
        # Print the basket's tare weight
        print(self.matchBasket().getTare())

    def displayPrice(self):
        # Print the basket's price
        print(self.matchBasket().getPrice())
        
    def displayNett(self):
        # Print the basket's net weight
        print(self.matchBasket().getNnett())

    def displayBasket(self):
        # Show the basket's content in the text area
        self.basket_content.insert(END, self.matchBasket())

    def getChoice(self, placeholder):
        # Set the selected basket based on dropdown choice
        self.selected_basket = str(self.combobox.get())
        print(self.selected_basket)

    def matchBasket(self):
        # Match the selected basket to its corresponding object
        match self.selected_basket:
            case "Basket 1":
                return basket_1
            case "Basket 2":
                return basket_2
            case "Basket 3":
                return basket_3
            case "Basket 4":
                return basket_4
            case "Basket 5":
                return basket_5
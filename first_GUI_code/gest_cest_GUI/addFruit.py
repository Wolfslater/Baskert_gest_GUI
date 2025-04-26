# Version 2.6.4 26/04/2925

from showWarning import showWarning, MISSINGBASKET, VALUEERROR
from dropDown import DropDown
from factory import Factory
from tkinter import END
from Frutto import Frutto
from baskets import (basket_1, basket_2, basket_3,
                     basket_4, basket_5, VALUES)

class addFruit:
    def __init__(self, master, relative, fruit):
        # Initialize the GUI elements and attributes
        self.master = master
        self.relative = relative
        self.fruit = fruit
        self.selected_basket = ""

        self.master.title("Fruit manager")  # Set title

        # Combobox for selecting a basket
        self.dropdown = DropDown(master, VALUES, self.dropdownHandler)
        self.dropdown.combobox.grid(row=0, column=0, padx=15)

        # Labels for inputs and last added fruit
        self.name_label = Factory.newLabel(self.master, text="Fruit name here:")
        self.price_label = Factory.newLabel(self.master, text="Fruit price (€/Kg) here:")
        self.weight_label = Factory.newLabel(self.master, text="Fruit weight (gr) here:")
        self.last_fruit_label = Factory.newLabel(self.master)

        # Labels layout
        Factory.gridConfig(widget=self.name_label, row=1, column=0)
        Factory.gridConfig(widget=self.price_label, row=2, column=0)
        Factory.gridConfig(widget=self.weight_label, row=3, column=0)
        Factory.gridConfig(widget=self.last_fruit_label, row=6, column=0, sticky="w")

        # Entry widgets for user input
        self.name_entry = Factory.newEntry(self.master, width=35)
        self.price_entry = Factory.newEntry(self.master, width=35)
        self.weight_entry = Factory.newEntry(self.master, width=35)

        # Entry layout
        Factory.gridConfig(widget=self.name_entry, row=1, column=1)
        Factory.gridConfig(widget=self.price_entry,row=2, column=1)
        Factory.gridConfig(widget=self.weight_entry, row=3, column=1)

        # Buttons for different actions
        self.add_btn = Factory.newButton(self.master, text="Add the fruit to the basket", command=self.insertFruit)
        self.back_btn = Factory.newButton(self.master, text="Back", command=self.back)
        self.clear_btn = Factory.newButton(self.master, text="Clear fruit entry infos", command=self.clearInfos)

        # Buttons layout
        Factory.gridConfig(widget=self.add_btn, row=4, column=1, padx=5, pady=5)
        Factory.gridConfig(widget=self.back_btn, row=5, column=0, padx=40, pady=5)
        Factory.gridConfig(widget=self.clear_btn, row=5, column=1, padx=5, pady=5)
    
    def back(self):
        # Return to the previous window
        self.relative.deiconify()
        self.master.destroy()
    
    def insertFruit(self):
        self.fruit = self.getFruit()

        try: 
            if self.fruit:
                self.fruit = Frutto(self.fruit)
            elif self.fruit is None:
                self.fruit = Frutto()

            if self.selected_basket:
                self.last_fruit_label.config(text="")
                self.last_fruit_label.config(text=
                f"Last added fruit: {self.fruit.getName()}")
                
                self.addToBasket()
            else:
                showWarning(MISSINGBASKET)
        except ValueError:
            showWarning(VALUEERROR)

    def dropdownHandler(self, event=None):
        selectedItem = self.dropdown.getBasket()
        if not selectedItem:
            self.dropdown.showBasketWarning()
        else:
            self.selected_basket = selectedItem

    def addToBasket(self):
        match self.selected_basket:
            case "Basket 1":
                basket_1.add(self.fruit)
            case "Basket 2":
                basket_2.add(self.fruit)
            case "Basket 3":
                basket_3.add(self.fruit)
            case "Basket 4":
                basket_4.add(self.fruit)
            case "Basket 5":
                basket_5.add(self.fruit)
    
    def getFruit(self):
        # Create a fruit object and display its name
        name = self.name_entry.get()
        price = self.price_entry.get()
        weight = self.weight_entry.get()
        return [name, price, weight]
    
    def clearInfos(self):
        # Clear the input fields
        for entry in [self.name_entry, self.price_entry, self.weight_entry]:
          entry.delete(0, END)
# Version 2.8.5 06/05/2025

from tkinter import END
from Frutto import Frutto
from widgets import (Warning, DropDown, Factory, VALUES, baskets)

class addFruit:
    def __init__(self, master, relative, fruit):
        # Initialize the GUI elements and attributes
        self.master = master
        self.relative = relative
        self.fruit = fruit
        self.selected_basket = ""
        self.name = Factory.newLabel
        self.entry = Factory.newEntry
        self.button = Factory.newButton
        self.grid = Factory.gridConfig

        self.master.title("Fruit manager")  # Set title

        # Combobox for selecting a basket
        self.dropdown = DropDown(self.master, VALUES, self.dropdownHandler)
        self.dropdown.combobox.grid(row=0, column=0, padx=15)

        # Labels for inputs and last added fruit
        self.name_label = self.name(self.master, text="Fruit name here:")
        self.price_label = self.name(self.master, text="Fruit price (€/Kg) here:")
        self.weight_label = self.name(self.master, text="Fruit weight (gr) here:")
        self.last_fruit_label = self.name(self.master)

        # Labels layout
        self.grid(widget=self.name_label, row=1, column=0)
        self.grid(widget=self.price_label, row=2, column=0)
        self.grid(widget=self.weight_label, row=3, column=0)
        self.grid(widget=self.last_fruit_label, row=6, column=0, sticky="w")

        # Entry widgets for user input
        self.name_entry = self.entry(self.master, width=35)
        self.price_entry = self.entry(self.master, width=35)
        self.weight_entry = self.entry(self.master, width=35)

        # Entry layout
        self.grid(widget=self.name_entry, row=1, column=1)
        self.grid(widget=self.price_entry,row=2, column=1)
        self.grid(widget=self.weight_entry, row=3, column=1)

        # Buttons for different actions
        self.add_btn = self.button(self.master, text="Add the fruit to the basket", command=self.insertFruit)
        self.back_btn = self.button(self.master, text="Back", command=self.back)
        self.clear_btn = self.button(self.master, text="Clear fruit entry infos", command=self.clearInfos)

        # Buttons layout
        self.grid(widget=self.add_btn, row=4, column=1, padx=5, pady=5)
        self.grid(widget=self.back_btn, row=5, column=0, padx=40, pady=5)
        self.grid(widget=self.clear_btn, row=5, column=1, padx=5, pady=5)
    
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
                Warning("1").showWarning()
        except ValueError:
            Warning("2").showWarning()

    def dropdownHandler(self, event=None):
        selectedItem = self.dropdown.getBasket()
        if selectedItem:
            self.selected_basket = selectedItem

    def addToBasket(self):
        baskets.addFruit(self.selected_basket, self.fruit)

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
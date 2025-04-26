# Version 2.6.3 26/04/2925

from dropDown import DropDown
from tkinter import Label, Button, END, Entry, messagebox
from Frutto import Frutto
from baskets import (basket_1, basket_2, basket_3,
                     basket_4, basket_5, values)

class addFruit:
    def __init__(self, master, relative, fruit):
        # Initialize the GUI elements and attributes
        self.master = master
        self.relative = relative
        self.fruit = fruit
        self.selected_basket = ""

        # Combobox for selecting a basket
        self.dropdown = DropDown(master, values, self.dropdownHandler)
        self.dropdown.combobox.grid(row=0, column=0, padx=15)

        # Labels for inputs and last added fruit
        self.name_label = Label(self.master, text="Fruit name here:")
        self.price_label = Label(self.master, text="Fruit price (€/Kg) here:")
        self.weight_label = Label(self.master, text="Fruit weight (gr) here:")
        self.last_fruit_label = Label(self.master)

        # Labels layout
        self.name_label.grid(row=1, column=0)
        self.price_label.grid(row=2, column=0)
        self.weight_label.grid(row=3, column=0)
        self.last_fruit_label.grid(row=6, column=0, sticky="w")

        # Entry widgets for user input
        self.name_entry = Entry(self.master, width=35)
        self.price_entry = Entry(self.master, width=35)
        self.weight_entry = Entry(self.master, width=35)

        # Entry layout
        self.name_entry.grid(row=1, column=1)
        self.price_entry.grid(row=2, column=1)
        self.weight_entry.grid(row=3, column=1)

        # Buttons for different actions
        self.add_btn = Button(self.master, text="Add the fruit to the basket", command=self.insertFruit)
        self.back_btn = Button(self.master, text="Back", command=self.back)
        self.clear_btn = Button(self.master, text="Clear fruit entry infos", command=self.clearInfos)

        # Buttons layout
        self.add_btn.grid(row=4, column=1, padx=5, pady=5)
        self.back_btn.grid(row=5, column=0, padx=40, pady=5)
        self.clear_btn.grid(row=5, column=1, padx=5, pady=5)
    
    def showEntryWarning(self):
        self.messagebox = messagebox.showwarning(
            "WARNING", "ERROR: " \
            "MISSING DATA OR WRONG DATA TYPE." \
            "\nPrice and weight must be numeric values.")
    
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
                self.dropdown.showWarning()
        except ValueError:
            self.showEntryWarning()

    def dropdownHandler(self, event=None):
        selectedItem = self.dropdown.getBasket()
        if not selectedItem:
            self.dropdown.showWarning()
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

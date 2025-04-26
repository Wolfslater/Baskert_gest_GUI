# Version 1.7.2 26/04/2025

from showWarning import showWarning, MISSINGBASKET
from dropDown import DropDown
from tkinter import Text
from factory import Factory
from addFruit import END
from baskets import (basket_1, basket_2, basket_3,
                     basket_4, basket_5, VALUES)

class BasketInfos:
    def __init__(self, master, relative):
        # Initialize the GUI components
        self.master = master
        self.relative = relative
        self.selected_basket = ""

        # Labels and text area for basket details - NOT disabled initially
        self.basket_content = Text(self.master, bg="#f0f0f0")

        # Buttons for actions
        self.backBtn = Factory.newButton(self.master, text="Back", command=self.back)
        self.tareBtn = Factory.newButton(self.master, text="Display tare", command=self.displayTare)
        self.netBtn = Factory.newButton(self.master, text="Display net", command=self.displayNett)
        self.basketBtn = Factory.newButton(self.master, text="Display basket", command=self.displayBasket)
        self.PricetBtn = Factory.newButton(self.master, text="Display basket's price", command=self.displayPrice)
        self.grossBtn = Factory.newButton(self.master, text="Display basket's gross weight",
                                                            command=self.displayGrossWeight)

        # Dropdown to select a basket
        self.dropdown = DropDown(master, VALUES, self.dropdownHandler)
        self.dropdown.combobox.grid(row=0, column=6, sticky="ew")

        # Arrange GUI components in a grid
        self.master.grid_columnconfigure(0, weight=1)  # Back button column
        self.master.grid_columnconfigure(1, weight=1)  # Tare button column
        self.master.grid_columnconfigure(2, weight=1)  # Nett button column
        self.master.grid_columnconfigure(3, weight=1)  # Gross weight column
        self.master.grid_columnconfigure(4, weight=1)  # Basket button column
        self.master.grid_columnconfigure(5, weight=1)  # Prize button column
        self.master.grid_columnconfigure(6, weight=1)  # Dropdown column

        # Place the Text widget in column 1 (adjust as needed)
        Factory.gridConfig(widget=self.basket_content,
        row=1, column=0, columnspan=6, sticky="nsew")  # Expand across multiple columns if necessary

        # Place the buttons and combobox
        Factory.gridConfig(widget=self.backBtn , row=0, column=0, sticky="ew")
        Factory.gridConfig(widget=self.tareBtn ,row=0, column=1, sticky="ew")
        Factory.gridConfig(widget=self.netBtn ,row=0, column=2, sticky="ew")
        Factory.gridConfig(widget=self.grossBtn, row=0, column=3, sticky="ew")
        Factory.gridConfig(widget=self.basketBtn, row=0, column=4, sticky="ew")
        Factory.gridConfig(widget=self.PricetBtn, row=0, column=5, sticky="ew")

    def back(self):
        # Go back to the previous window
        self.relative.deiconify()
        self.master.destroy()
        
    def update_text_display(self, content):
        # Helper function to update text and make it read-only
        self.basket_content.config(state="normal")  # Ensure it's editable first
        self.basket_content.delete("1.0", "end")    # Clear existing content
        self.basket_content.insert(END, content)    # Add new content
        self.basket_content.config(state="disabled") # Make read-only
    
    def displayGrossWeight(self):
        if self.matchBasket():
            self.gross = self.matchBasket().getGrossWeight()
            self.update_text_display(f"Basket's gross weight is: {self.gross}gr")

    def displayTare(self):
        if self.matchBasket(): 
        # Print the basket's tare weight
            self.tare = self.matchBasket().getTare()
            self.update_text_display(f"Basket's tare is: {self.tare}gr")

    def displayPrice(self):
        if self.matchBasket(): 
            # Print the basket's price
            self.price = self.matchBasket().getPrice()
            self.update_text_display(f"Basket's total price is: {self.price}€")
            
    def displayNett(self):
        if self.matchBasket(): 
            # Print the basket's net weight
            self.nett = self.matchBasket().getNett()
            self.update_text_display(f"Basket's nett is: {self.nett}gr")
        
    def displayBasket(self):
        if self.matchBasket(): 
            # Show the basket's content in the text area
            self.update_text_display(str(self.matchBasket()))
    
    def dropdownHandler(self, event=None):
        selectedItem = self.dropdown.getBasket()
        if selectedItem:
            self.selected_basket = selectedItem

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
            case _:
                showWarning(MISSINGBASKET)
                return None

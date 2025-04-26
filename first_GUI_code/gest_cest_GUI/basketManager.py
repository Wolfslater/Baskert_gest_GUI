# Version 1.7.0 26/04/2025

from dropDown import DropDown
from tkinter import Text
from addFruit import Button, END, messagebox
from baskets import (basket_1, basket_2, basket_3,
                     basket_4, basket_5, values)

class BasketInfos:
    def __init__(self, master, relative):
        # Initialize the GUI components
        self.master = master
        self.relative = relative
        self.selected_basket = ""

        # Labels and text area for basket details - NOT disabled initially
        self.basket_content = Text(self.master, bg="#f0f0f0")

        # Buttons for actions
        self.backBtn = Button(self.master, text="Back", command=self.back)
        self.tareBtn = Button(self.master, text="Display tare", command=self.displayTare)
        self.nettBtn = Button(self.master, text="Display nett", command=self.displayNett)
        self.basketBtn = Button(self.master, text="Display basket", command=self.displayBasket)
        self.PrizetBtn = Button(self.master, text="Display basket's price", command=self.displayPrice)
        self.grossBtn = Button(self.master, text="Display basket's gross weight",
                               command=self.displayGrossWeight)

        # Dropdown to select a basket
        self.dropdown = DropDown(master, values, self.dropdownHandler)
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
        self.basket_content.grid(row=1, column=0, columnspan=6, sticky="nsew")  # Expand across multiple columns if necessary

        # Place the buttons and combobox
        self.backBtn.grid(row=0, column=0, sticky="ew")
        self.tareBtn.grid(row=0, column=1, sticky="ew")
        self.nettBtn.grid(row=0, column=2, sticky="ew")
        self.grossBtn.grid(row=0, column=3, sticky="ew")
        self.basketBtn.grid(row=0, column=4, sticky="ew")
        self.PrizetBtn.grid(row=0, column=5, sticky="ew")

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
        if not selectedItem:
            self.dropdown.showWarning()
        else:
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

# Version 1.9.2 06/05/2025

from tkinter import Text
from tkinter import END
from widgets import (Warning, DropDown, Factory, VALUES, baskets)

class BasketInfos:
    def __init__(self, master, relative):
        # Initialize the GUI components
        self.master = master
        self.relative = relative
        self.selected_basket = ""
        self.button = Factory.newButton
        self.grid = Factory.gridConfig

        self.master.title("Basket manager")  # Set title

        # Labels and text area for basket details - NOT disabled initially
        self.basket_content = Text(self.master, bg="#f0f0f0")

        # Buttons for actions
        self.backBtn = self.button(self.master, text="Back", command=self.back)
        self.tareBtn = self.button(self.master, text="Display tare", command=self.displayTare)
        self.netBtn = self.button(self.master, text="Display net", command=self.displayNet)
        self.basketBtn = self.button(self.master, text="Display basket", command=self.displayBasket)
        self.PricetBtn = self.button(self.master, text="Display basket's price", command=self.displayPrice)
        self.grossBtn = self.button(self.master, text="Display basket's gross weight",
                                                            command=self.displayGrossWeight)
        # Dropdown to select a basket
        self.dropdown = DropDown(master, VALUES, self.dropdownHandler)
        self.grid(widget=self.dropdown.combobox, row=0, column=6, sticky="ew")

        # Arrange GUI components in a grid
        self.master.grid_columnconfigure(0, weight=1)  # Back button column
        self.master.grid_columnconfigure(1, weight=1)  # Tare button column
        self.master.grid_columnconfigure(2, weight=1)  # Net button column
        self.master.grid_columnconfigure(3, weight=1)  # Gross weight column
        self.master.grid_columnconfigure(4, weight=1)  # Basket button column
        self.master.grid_columnconfigure(5, weight=1)  # Prize button column
        self.master.grid_columnconfigure(6, weight=1)  # Dropdown column

        # Place the Text widget in column 1 (adjust as needed)
        self.grid(widget=self.basket_content,
        row=1, column=0, columnspan=6, sticky="nsew")  # Expand across multiple columns if necessary

        # Place the buttons and combobox
        self.grid(widget=self.backBtn , row=0, column=0, sticky="ew")
        self.grid(widget=self.tareBtn ,row=0, column=1, sticky="ew")
        self.grid(widget=self.netBtn ,row=0, column=2, sticky="ew")
        self.grid(widget=self.grossBtn, row=0, column=3, sticky="ew")
        self.grid(widget=self.basketBtn, row=0, column=4, sticky="ew")
        self.grid(widget=self.PricetBtn, row=0, column=5, sticky="ew")

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
        if self.getBasketName():
            self.gross = self.getBasketName().getGrossWeight()
            self.update_text_display(f"Basket's gross weight is: {self.gross}gr")

    def displayTare(self):
        if self.getBasketName(): 
        # Print the basket's tare weight
            self.tare = self.getBasketName().getTare()
            self.update_text_display(f"Basket's tare is: {self.tare}gr")

    def displayPrice(self):
        if self.getBasketName(): 
            # Print the basket's price
            self.price = self.getBasketName().getPrice()
            self.update_text_display(f"Basket's total price is: {self.price}€")
            
    def displayNet(self):
        if self.getBasketName(): 
            # Print the basket's net weight
            self.net = self.getBasketName().getNet()
            self.update_text_display(f"Basket's net is: {self.net}gr")
        
    def displayBasket(self):
        if self.getBasketName(): 
            # Show the basket's content in the text area
            self.update_text_display(str(self.getBasketName()))
    
    def dropdownHandler(self, event=None):
        selectedItem = self.dropdown.getBasket()
        if selectedItem:
            self.selected_basket = selectedItem

    def getBasketName(self):
        return baskets.getBasket(self.selected_basket)

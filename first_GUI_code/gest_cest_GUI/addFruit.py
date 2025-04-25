# Version 2.5.0 24/04/2925

from tkinter.ttk import Combobox
from tkinter import Label, Button, END, Entry, messagebox
from Frutto import Frutto
from baskets import (basket_1, basket_2, 
                     basket_3, basket_4, basket_5)

class addFruit:
    def __init__(self, master, relative, fruit):
        # Initialize the GUI elements and attributes
        self.master = master
        self.relative = relative
        self.fruit = fruit
        self.selected_basket = ""

        # Combobox for selecting a basket
        self.combobox = Combobox(self.master, width=45)
        self.combobox['values'] = ["Basket 1", "Basket 2", "Basket 3", "Basket 4", "Basket 5"]
        self.combobox["state"] = "readonly"
        self.combobox.bind("<<ComboboxSelected>>", self.getChoice)
        self.combobox.grid(row=0, column=0, padx=15, pady=5)

        # Labels for inputs and last added fruit
        self.name_label = Label(self.master, text="Fruit name here:")
        self.prize_label = Label(self.master, text="Fruit price (€/Kg) here:")
        self.weight_label = Label(self.master, text="Fruit weight (gr) here:")
        self.last_fruit_label = Label(self.master)

        # Labels layout
        self.name_label.grid(row=1, column=0)
        self.prize_label.grid(row=2, column=0)
        self.weight_label.grid(row=3, column=0)
        self.last_fruit_label.grid(row=6, column=0, sticky="w")

        # Entry widgets for user input
        self.name_entry = Entry(self.master, width=35)
        self.prize_entry = Entry(self.master, width=35)
        self.weight_entry = Entry(self.master, width=35)

        # Entry layout
        self.name_entry.grid(row=1, column=1)
        self.prize_entry.grid(row=2, column=1)
        self.weight_entry.grid(row=3, column=1)

        # Buttons for different actions
        self.add_btn = Button(self.master, text="Add the fruit to the basket", command=self.insertFruit)
        self.back_btn = Button(self.master, text="Back", command=self.back)
        self.clear_btn = Button(self.master, text="Clear fruit entry infos", command=self.clearInfos)

        # Buttons layout
        self.add_btn.grid(row=4, column=1, padx=5, pady=5)
        self.back_btn.grid(row=5, column=0, padx=40, pady=5)
        self.clear_btn.grid(row=5, column=1, padx=5, pady=5)
    
    def showBasketWarning(self):
        self.messagebox = messagebox.showwarning(
            "WARNING", "Select a basket first")
        
    def showEntryWarning(self):
        self.messagebox = messagebox.showwarning(
            "WARNING", "Fill all fruit data"
        )

    def back(self):
        # Return to the previous window
        self.relative.deiconify()
        self.master.destroy()

    def getChoice(self, placeholder):
        # Get the selected basket
        self.selected_basket = str(self.combobox.get())
    
    def insertFruit(self):
        self.fruit = self.getFruit()
        
        try: 
            if self.fruit is not None:
                self.fruit = Frutto(self.fruit)
            elif self.fruit is None:
                self.fruit = Frutto()

            if self.selected_basket:
                self.last_fruit_label.config(text="")
                self.last_fruit_label.config(text=
                f"Last added fruit: {self.fruit.getName()}")
                
                self.addToBasket()
            else:
                self.showBasketWarning()
        except ValueError:
            self.showEntryWarning()
    
    def addToBasket(self):
        # Add the fruit to the selected basket
        if not self.selected_basket: 
            self.showBasketWarning()
        
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
        prize = self.prize_entry.get()
        weight = self.weight_entry.get()
        return [name, prize, weight]
    
    def clearInfos(self):
        # Clear the input fields
        self.name_entry.delete(0, END)
        self.prize_entry.delete(0, END)
        self.weight_entry.delete(0, END)

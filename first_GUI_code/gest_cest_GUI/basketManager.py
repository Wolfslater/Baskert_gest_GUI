#Version 1.5.2 21/04/2025

from addFrutto import Combobox, Button
from baskets import (basket_1, basket_2, 
                     basket_3, basket_4, basket_5)

class BasketInfos:
    def __init__(self, master, relative):
        self.master = master
        self.relative = relative
        self.selected_basket = ""

        self.backBtn = Button(self.master, text="Back", command=self.back)
        self.taraBtn = Button(self.master, text="Disply tara", command=self.displaytara)
        self.nettoBtn = Button(self.master, text="Disply netto", command=self.displayNetto)
        self.basketBtn = Button(self.master, text="Disply basket", command=self.displayBasket)
        self.PrizetBtn = Button(self.master, text="Disply basket's prize", command=self.displayPrice)


        self.combobox = Combobox(self.master)
        self.combobox["values"] = ["Basket 1", "Basket 2", "Basket 3", "Basket 4", "Basket 5"]
        self.combobox["state"] = "readonly"
        self.combobox.bind("<<ComboboxSelected>>", self.getChoice)

        self.combobox.grid(row=1, column=0, padx=15, pady=5, columnspan=10)

        self.backBtn.grid(row=0, column=0, padx=15, pady=15)
        self.taraBtn.grid(row=0, column=1, padx=15, pady=15)
        self.nettoBtn.grid(row=0, column=2, padx=15, pady=15)
        self.basketBtn.grid(row=0, column=3, padx=15, pady=15)
        self.PrizetBtn.grid(row=0, column=4, padx=15, pady=15)

    def back(self):
        self.relative.deiconify()
        self.master.destroy()

    def displaytara(self):
        print(self.matchBasket().getTara())

    def displayPrice(self):
        print(self.matchBasket().costo())
        
    def displayNetto(self):
        print(self.matchBasket().netto())

    def displayBasket(self):
        print(self.matchBasket())

    def getChoice(self, placeholder):
        self.selected_basket = str(self.combobox.get())
        print(self.selected_basket)

    def matchBasket(self):
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
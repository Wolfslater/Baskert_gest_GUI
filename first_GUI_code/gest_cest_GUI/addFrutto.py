from tkinter import *
from tkinter.ttk import *   
from Cestino import *
from Frutto import *
from baskets import basket_1, basket_2, basket_3, basket_4, basket_5

class addFruit:
    def __init__(self, master, parent, fruit):
        self.master = master
        self.parent = parent
        self.fruit = fruit
        self.frame = Frame(self.master)
        self.master.geometry("600x250")
        self.master.title("Fuit infos")
        self.selected_basket = ""
        
        self.combobox = Combobox(self.master, width=45)
        self.combobox['values'] = ["Basket 1", "Basket 2", "Basket 3", "Basket 4", "Basket 5"]
        self.combobox.grid(row=0, column=0, padx=15, pady=5)
        self.combobox["state"] = "readonly"
        self.combobox.bind("<<ComboboxSelected>>", self.getChoice)

        self.name_label = Label(self.master, text="Fruit name here:")
        self.name_label.grid(row=1, column=0)
        self.name_entry = Entry(self.master, width=35)
        self.name_entry.grid( row=1, column=1)

        self.prize_label = Label(self.master, text="Fruit prize (€/Kg) here:")
        self.prize_label.grid(row=2, column=0)
        self.prize_entry = Entry(self.master, width=35)
        self.prize_entry.grid( row=2, column=1)

        self.weight_label = Label(self.master, text="Fruit weight (gr) here:")
        self.weight_label.grid(row=3, column=0)
        self.weight_entry = Entry(self.master, width=35)
        self.weight_entry.grid( row=3, column=1)

        self.addBtn = Button(self.master, text="Add the ftuit to the basket", command=self.insertFruit)
        self.addBtn.grid(column=0, row=4, padx=5, pady=5)

        self.backBtn = Button(self.master, text="back", command=self.back)
        self.backBtn.grid(row=5, column=1, padx=40, pady=5)

        self.clearBtn = Button(self.master, text="Clear all fruit infos", command=self.clearInfos)
        self.clearBtn.grid(row=4, column=1, padx=5, pady=5)

    def back(self):
        self.parent.deiconify()
        self.master.destroy()

    def getChoice(self, placeholder):
        self.selected_basket = str(self.combobox.get())
        print(self.selected_basket)
    
    def insertFruit(self):
        name = self.name_entry.get()
        prize = self.prize_entry.get()
        weight = self.weight_entry.get()
        self.fruit = [name, prize, weight]
        print(self.fruit)
        if self.fruit is not None:
            self.fruit = Frutto(self.fruit)
        else:
            self.fruit = Frutto()
        self.addToBasket()

        return self.fruit
    
    def addToBasket(self):
        if not self.selected_basket: print("Select a basket first!")
        match self.selected_basket:
            case "Basket 1":
                basket_1.add(self.fruit)
                print(basket_1)
            case "Basket 2":
                basket_2.add(self.fruit)
                print(basket_2)
            case "Basket 3":
                basket_3.add(self.fruit)
                print(basket_3)
            case "Basket 4":
                basket_4.add(self.fruit)
                print(basket_4)
            case "Basket 5":
                basket_5.add(self.fruit)
                print(basket_5)

    def clearInfos(self):
        self.name_entry.delete(0, END)
        self.prize_entry.delete(0, END)
        self.weight_entry.delete(0, END)

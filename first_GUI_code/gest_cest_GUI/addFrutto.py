from tkinter import *
from tkinter.ttk import *   
from Cestino import *
from Frutto import *

class addFruit:
    def __init__(self, master, parent, fruit):
        self.master = master
        self.parent = parent
        self.fruit = fruit
        self.frame = Frame(self.master)
        self.master.geometry("600x250")
        self.master.title("Fuit infos")
        
        self.combobox = Combobox(self.master, width=45)
        self.combobox['values'] = ["Cesta 1", "Cesta 2", "Cesta 3", "Cesta 4", "Cesta 5"]
        self.combobox.grid(row=0, column=0, padx=15, pady=5)
        self.combobox["state"] = ["readonly"]
        choice = self.combobox.bind("<<ComboboxSelected>>", self.getChoice)

        self.name_label = Label(self.master, text="Fruit name here:")
        self.name_label.grid(row=1, column=0)
        self.name_entry = Entry(self.master, width=35)
        self.name_entry.grid( row=1, column=1)

        self.pize_label = Label(self.master, text="Fruit name prize:")
        self.pize_label.grid(row=2, column=0)
        self.prize_entry = Entry(self.master, width=35)
        self.prize_entry.grid( row=2, column=1)

        self.wehight_label = Label(self.master, text="Fruit name wehight:")
        self.wehight_label.grid(row=3, column=0)
        self.wehight_entry = Entry(self.master, width=35)
        self.wehight_entry.grid( row=3, column=1)

        self.backBtn = Button(self.master, text="back", command=self.back)
        self.backBtn.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    def back(self):
        self.parent.deiconify()
        self.master.destroy()

    def getChoice(self, placeholder):
        selected = self.combobox.get()
        print(selected)
        return selected
    
    def createBasket(self, choice):
        pass
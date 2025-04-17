from tkinter import *
from tkinter.ttk import *   
from Cestino import *
from Frutto import *

class addFruit:
    def __init__(self, master, parent, fruit):
        self.master = master
        self.father = parent
        self.fruit = fruit
        self.frame = Frame(self.master)
        self.master.geometry("800x600")
        self.master.title("Fuit infos")


from addFrutto import *

class gestionaleGUI:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry("800x600")
        self.master.title("Gestionale GUI cestini di frutta")

        self.addBtn = Button(self.master, text="Add fruit to the basket.", command=self.add)
        self.exitBtn = Button(self.master, text="Exit the the program.", command=self.exit)
        self.addBtn.grid(row=0, column=0, padx=50, pady=0)
        self.exitBtn.grid(row=0, column=1, padx=15, pady=0)

        self.fruit = Frutto()

    def add(self):
        self.newWindow = Toplevel(self.master)
        addFruit(self.newWindow, self.master, self.fruit)

    def exit(self):
        exit()
from addFrutto import *

class gestionaleGUI:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry("800x600")
        self.master.title("Gestionale GUI cestini di frutta")
        self.addBtn = Button(self.master, text="Add fruit to the basket.", command=self.add)
        self.exitBtn = Button(self.master, text="Exit the the program.", command=self.exit)

        self.addBtn.pack()
        self.exitBtn.pack()
        self.frame.pack()

        self.fruit = Frutto()

    def add(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        new_fruit = addFruit(self.master, self.newWindow, self.fruit)

    def exit(self):
        exit()
# Version 2.3.6 06/05/2025

from tkinter import Toplevel, Tk
from Frutto import Frutto
from addFruit import addFruit
from widgets import Factory
from basketManager import BasketInfos

class GUIManagement:
    def __init__(self, master):
        self.master = master
        self.grid = Factory.gridConfig
        self.button = Factory.newButton
        self.master.geometry("600x200")  # Set window size
        self.master.title("Main page")  # Set title

        # Buttons with commands
        self.addBtn = self.button(self.master, text="Add fruit to the basket.", command=self.add)
        self.exitBtn = self.button(self.master, text="Exit the the program.", command=self.exit)
        self.basketBtn = self.button(self.master, text="Open basket manager", command=self.basketManager)

        # Layout
        self.grid(widget=self.addBtn, row=0, column=0, padx=50)
        self.grid(widget=self.exitBtn, row=0, column=1, padx=15)
        self.grid(widget=self.basketBtn, row=0, column=2, padx=50)

        self.fruit = Frutto()  # Initialize fruit object

    def add(self):  # Open add fruit window
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        addFruit(self.newWindow, self.master, self.fruit)

    def exit(self):  # Exit program
        exit()

    def basketManager(self):  # Open basket manager
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        BasketInfos(self.newWindow, self.master)

if __name__ == '__main__':
    # Create the main application window (root window).
    root = Tk()
    # Instantiate the GUIManagement class, passing the root window as an argument.
    GUIManagement(root)
    # Start the Tkinter event loop to keep the application running and responsive.
    root.mainloop()
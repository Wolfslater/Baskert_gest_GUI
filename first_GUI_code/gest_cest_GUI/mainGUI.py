# Version 0.2.3 21/04/2025

# Import the GUIManagement class from the GUImanagement module.
from GUImanagement import GUIManagement
# Import the Tk class from the tkinter library, which is used to create the main application window.
from tkinter import Tk

# The main entry point of the program.
if __name__ == '__main__':
    # Create the main application window (root window).
    root = Tk()
    # Instantiate the GUIManagement class, passing the root window as an argument.
    GUIManagement(root)
    # Start the Tkinter event loop to keep the application running and responsive.
    root.mainloop()
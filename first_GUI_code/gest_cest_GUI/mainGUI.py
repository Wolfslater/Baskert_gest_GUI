# Version 0.2.3 21/04/2925

from GUImanagement import GUIManagement
from tkinter import Tk

if __name__ == '__main__':
    # Create the main application window (root window).
    root = Tk()
    # Instantiate the GUIManagement class, passing the root window as an argument.
    GUIManagement(root)
    # Start the Tkinter event loop to keep the application running and responsive.
    root.mainloop()
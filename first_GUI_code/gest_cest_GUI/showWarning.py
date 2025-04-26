#Version 0.0.1 26/04/2025

from tkinter import messagebox

def showWarning(message):
    messagebox.showwarning("WARNING", message)

MISSINGBASKET = "Please select a basket first"
VALUEERROR = "ERROR: " \
            "MISSING DATA OR WRONG DATA TYPE." \
            "\nPrice and weight must be numeric values."
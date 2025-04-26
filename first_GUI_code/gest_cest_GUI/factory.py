#version 0.0.1 26/04/2025

from tkinter import Label, Button, Entry

class Factory:
    def __init__(self, master):
        master = master

    def newLabel(master, text=None):
        label = Label(master, text=text)
        return label

    def newEntry(master, width=0):
        entry = Entry(master, width=width)
        return entry

    def newButton(master, text=None, command=None):
        button = Button(master, text=text, command=command)
        return button

    def gridConfig(widget, row, column, padx=0, pady=0, sticky="", columnspan=1):
        widget.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky, columnspan=columnspan)
        return widget
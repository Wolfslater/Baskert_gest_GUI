#version 0.0.2 26/04/2025

from tkinter import Label, Button, Entry

class Factory:
    @staticmethod
    def __init__(master):
        master = master

    @staticmethod
    def newLabel(master, text=None):
        label = Label(master, text=text)
        return label

    @staticmethod
    def newEntry(master, width=0):
        entry = Entry(master, width=width)
        return entry

    @staticmethod
    def newButton(master, text=None, command=None):
        button = Button(master, text=text, command=command)
        return button

    @staticmethod
    def gridConfig(widget, row, column, padx=0, pady=0, sticky="", columnspan=1):
        widget.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky, columnspan=columnspan)
        return widget

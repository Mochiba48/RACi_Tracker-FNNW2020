import csv
from tkinter import *
from datetime import time
import time
import GUI
import Tracker
import Kategorien


def buttonAufgabenClick():
    GUI.AufgabenErfassen()


def buttonTrackenClick():
    Tracker.TrackerStarten()


def buttonAuswertenClick():
    import Auswertung


def buttonKategorienClick():
    Kategorien.Kategorie()


# Aktivierung des Fensters
root = Tk()
root.geometry('500x350')
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Aufgaben", command=buttonAufgabenClick)
filemenu.add_command(label="Tracken", command=buttonTrackenClick)
filemenu.add_command(label="Auswerten", command=buttonAuswertenClick)
filemenu.add_command(label="Kategorien", command=buttonKategorienClick)
filemenu.add_separator()
filemenu.add_command(label="Beenden", command=root.destroy)



buttonAufgaben = Button(master=root, text='Aufgabe erfassen', command=buttonAufgabenClick)
buttonAufgaben.place(x=40, y=240, width=100, height=40)

buttonAufgaben = Button(master=root, text='Tracken', command=buttonTrackenClick)
buttonAufgaben.place(x=200, y=240, width=100, height=40)

buttonAufgaben = Button(master=root, text='Auswerten', command=buttonAuswertenClick)
buttonAufgaben.place(x=360, y=240, width=100, height=40)


root.mainloop()
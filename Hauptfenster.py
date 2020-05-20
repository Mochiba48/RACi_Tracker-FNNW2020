import csv
from tkinter import *
from datetime import time
import time
import Aufgaben
import Tracker
import Kategorien
import AuswertungDatum
import AuswertungAufgaben


def buttonAufgabenClick():
    Aufgaben.AufgabenErfassen()


def buttonTrackenClick():
    Tracker.TrackerStarten()


def buttonAAuswertenClick():
    AuswertungAufgaben.AufgabenAuswerten()


def buttonZAuswertenClick():
    AuswertungDatum.Zeitauswertung()


def buttonKategorienClick():
    Kategorien.Kategorie()


# Aktivierung des Fensters
root = Tk()
root.geometry('520x320')
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Aufgaben", command=buttonAufgabenClick)
filemenu.add_command(label="Tracken", command=buttonTrackenClick)
filemenu.add_command(label="Aufgabe auswerten", command=buttonAAuswertenClick)
filemenu.add_command(label="Zeiten auswerten", command=buttonZAuswertenClick)
filemenu.add_command(label="Kategorien", command=buttonKategorienClick)
filemenu.add_separator()
filemenu.add_command(label="Beenden", command=root.destroy)

# Uhrzeit anzeigen
uhr = Label(master=root)
uhr.place(x=5, y=295)

zeit = ''
# Abfrage der Zeit vom laufenden Computer
# mit config wird das Label neu beschriftet
# mit after wird nach 0,2sek die Funktion tick neu aufgerufen
def tick():
    global zeit
    neuezeit = time.strftime("%d.%m.%Y %H:%M")
    if neuezeit != zeit:
        zeit = neuezeit
        uhr.config(text=zeit)
    uhr.after(200, tick)

logo= PhotoImage(file="RACI-Tracker.gif")
Label_logo = Label(root, image=logo)
Label_logo.place(x=0, y=0)


buttonAufgaben = Button(master=root, text='Aufgabe erfassen', command=buttonAufgabenClick)
buttonAufgaben.place(x=40, y=240, width=100, height=50)

buttonTracken = Button(master=root, text='Tracken', command=buttonTrackenClick)
buttonTracken.place(x=200, y=240, width=100, height=50)

buttonAAuswertenAufgabe = Button(master=root, text='Aufgabe auswerten', command=buttonAAuswertenClick)
buttonAAuswertenAufgabe.place(x=360, y=240, width=120, height=23)

buttonZAuswertenAufgabe = Button(master=root, text='Zeiten auswerten', command=buttonZAuswertenClick)
buttonZAuswertenAufgabe.place(x=360, y=267, width=120, height=23)

tick()
root.mainloop()
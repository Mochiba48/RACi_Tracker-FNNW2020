# import csv
from tkinter import *
from datetime import time
import time
import Aufgaben
import Tracker
import Kategorien
import AuswertungDatum
import AuswertungAufgaben

print("Test")
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
root.geometry('861x360')
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
uhr.place(x=5, y=335)

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

logo = PhotoImage(file="RACI-Tracker.gif")
canvasHintergrund = Canvas(master=root)
canvasHintergrund.place(x=0, y=0, width=861, height=278)
canvasHintergrund.create_image(0, 0, image=logo, anchor='nw')


buttonAufgaben = Button(master=root, text='Aufgabe erfassen', command=buttonAufgabenClick)
buttonAufgaben.place(x=270, y=290, width=100, height=50)

buttonTracken = Button(master=root, text='Tracken', command=buttonTrackenClick)
buttonTracken.place(x=380.5, y=290, width=100, height=50)

buttonAAuswertenAufgabe = Button(master=root, text='Aufgabe auswerten', command=buttonAAuswertenClick)
buttonAAuswertenAufgabe.place(x=490, y=290, width=120, height=23)

buttonZAuswertenAufgabe = Button(master=root, text='Zeiten auswerten', command=buttonZAuswertenClick)
buttonZAuswertenAufgabe.place(x=490, y=317, width=120, height=23)

tick()
root.mainloop()
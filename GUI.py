import csv
from tkinter import *
# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('RACi Tracker')
tkFenster.geometry('350x500')
# Aktivierung des Fensters

#Titel anzeigen
labeltitel = Label(master=tkFenster, text='Aufgabenerfassung', fg='black', font=('Arial', 16))
labeltitel.place(x=0, y=5, width=350, height=30)

#Daten eingeben
# Benennung
labelBenennung = Label(master=tkFenster, text='Benennung')
labelBenennung.place(x=10, y=40, width=100, height=27)
# Entry
entryBenennung = Entry(master=tkFenster, bg='white')
entryBenennung.place(x=120, y=40, width=200, height=27)

#BeschreibungTextfeld
labelBeschreibung = Label(master=tkFenster, text='Beschreibung')
labelBeschreibung.place(x=10, y=70, width=100, height=27)
# Entry
TextBeschreibung = Text(master=tkFenster, width=23, height=6, font=('Calibri', 10))
TextBeschreibung.place(x=120, y=70)
scrollbarBeschreibung = Scrollbar(master=tkFenster)
scrollbarBeschreibung.place(x=310, y=70, width=10, height=100)
TextBeschreibung.config(yscrollcommand=scrollbarBeschreibung.set)
scrollbarBeschreibung.config(command=TextBeschreibung.yview)

print(TextBeschreibung)

#Kategorie
labelKategorie = Label(master=tkFenster, text='Kategorie')
labelKategorie.place(x=10, y=180, width=100, height=27)
# Entry
entryKategorie = Entry(master=tkFenster, bg='white')
entryKategorie.place(x=120, y=180, width=200, height=27)


# Button zum Speichern
def buttonSpeichernClick():
    # Übernahme der Daten
    Benennung = str(entryBenennung.get())
    Beschreibung = TextBeschreibung.get('1.0', 'end').strip()
    Kategorie = str(entryKategorie.get())
    liste = [Benennung, Beschreibung, Kategorie]
    aufgaben_listeexp(liste)
    print(liste)

buttonSpeichern = Button(master=tkFenster, bg='#FBD975', text='Speichern', command=buttonSpeichernClick)
buttonSpeichern.place(x=120, y=210, width=100, height=27)

def aufgaben_listeexp(daten):
    with open('Aufgaben.csv', mode='a', newline='') as aufgaben_file:
        aufgaben_writer = csv.writer(aufgaben_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        aufgaben_writer.writerow(daten)

tkFenster.mainloop()
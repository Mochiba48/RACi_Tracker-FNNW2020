import csv
from tkinter import *
import CSV

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
TextBeschreibung = Text(master=tkFenster, width=25, height=6, font=('Calibri', 10))
TextBeschreibung.place(x=120, y=70)
# Scrollbar
scrollbarBeschreibung = Scrollbar(master=tkFenster)
scrollbarBeschreibung.place(x=310, y=70, width=10, height=100)
TextBeschreibung.config(yscrollcommand=scrollbarBeschreibung.set)
scrollbarBeschreibung.config(command=TextBeschreibung.yview)

kategorie = ["Simon", "Dani", "Kesh"]

#Kategorie
labelKategorie = Label(master=tkFenster, text='Kategorie')
labelKategorie.place(x=10, y=180, width=100, height=27)
# Listbox
listboxKategorie = Listbox(master=tkFenster, selectmode='browse')
for i in kategorie:
    listboxKategorie.insert('end', i)
listboxKategorie.place(x=120, y=180, width=180, height=50)
# Scroolbar
yScroll = Scrollbar(master=tkFenster, orient='vertical')
yScroll.place(x=310, y=180, width=10, height=50)
listboxKategorie.config(yscrollcommand=yScroll.set)
yScroll.config(command=listboxKategorie.yview)


# Button zum Speichern
def buttonSpeichernClick():
    # Übernahme der Daten
    Benennung = str(entryBenennung.get())
    Beschreibung = TextBeschreibung.get('1.0', 'end').strip()
    Kategorie = listboxKategorie.get(listboxKategorie.curselection())
    liste = [Benennung, Beschreibung, Kategorie]
    CSV.aufgaben_listeexp(liste)
    print(liste)
    # Ereignisbehandlung
    def buttonOkClick():
        tkFensterBestätigen.quit()
        tkFensterBestätigen.destroy()
    # Neues Fenster öffnen
    tkFensterBestätigen = Toplevel()
    tkFensterBestätigen.title('Information')
    tkFensterBestätigen.geometry('200x80')
    # Label mit der Bestätigung
    labelBestätigen = Label(master=tkFensterBestätigen, text='Aufgabe wurde gespeichert')
    labelBestätigen.place(x=25, y=5, width=150, height=20)
    # Button zum Schließen des Fensters
    buttonOk = Button(master=tkFensterBestätigen, text='ok',
                      command=buttonOkClick)
    buttonOk.place(x=60, y=35, width=80, height=30)

buttonSpeichern = Button(master=tkFenster, bg='#FBD975', text='Speichern', command=buttonSpeichernClick)
buttonSpeichern.place(x=120, y=240, width=100, height=27)

tkFenster.mainloop()
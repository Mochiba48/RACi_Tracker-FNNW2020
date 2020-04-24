import csv
from tkinter import *
import CSV


# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Kategorien')
tkFenster.geometry('500x300')
# Aktivierung des Fensters

#Titel anzeigen
labeltitel = Label(master=tkFenster, text='Kategorien erfassen', fg='black', font=('Arial', 16))
labeltitel.place(x=0, y=5, width=400, height=30)

#Kategorien anzeigen
#Kategorie
labelKategorie = Label(master=tkFenster, text='erfasste Kategorien')
labelKategorie.place(x=0, y=40, width=200, height=27)
# Listbox
listboxKategorie = Listbox(master=tkFenster, selectmode='browse')
with open('Kategorie.csv') as f:
    reader =csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data = list(reader)
for i in range(len(data)):
    data1 = data[i]
    listboxKategorie.insert('end',data1)
listboxKategorie.place(x=5, y=65, width=190, height=100)
# Scroolbar
yScroll = Scrollbar(master=tkFenster, orient='vertical')
yScroll.place(x=190, y=65, width=10, height=100)
listboxKategorie.config(yscrollcommand=yScroll.set)
yScroll.config(command=listboxKategorie.yview)

#neue Kategorie erfassen
#Daten eingeben
# Benennung
labelKategorie = Label(master=tkFenster, text='Kategorie erfassen')
labelKategorie.place(x=220, y=40, width=100, height=27)
# Entry
entryKategorie = Entry(master=tkFenster, bg='white')
entryKategorie.place(x=220, y=65, width=200, height=27)


# Button zum erfassen
def buttonSpeichernClick():
    # Übernahme der Daten

    eingabeKategorie = str(entryKategorie.get())
    liste = [eingabeKategorie]
    CSV.kategorie_listeexp(liste)
    with open('Kategorie.csv') as f:
        reader = csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data = list(reader)
    dataneu = data[-1]
    listboxKategorie.insert('end', dataneu)
    # Ereignisbehandlung
    def buttonOkClick():
        tkFensterBestätigen.destroy()
    # Neues Fenster öffnen
    tkFensterBestätigen = Toplevel()
    tkFensterBestätigen.title('Information')
    tkFensterBestätigen.geometry('200x80')
    # Label mit der Bestätigung
    labelBestätigen = Label(master=tkFensterBestätigen, text='Kategorie wurde gespeichert')
    labelBestätigen.place(x=25, y=5, width=150, height=20)
    # Button zum Schließen des Fensters
    buttonOk = Button(master=tkFensterBestätigen, text='ok',
                      command=buttonOkClick)
    buttonOk.place(x=60, y=35, width=80, height=30)



buttonSpeichern = Button(master=tkFenster, bg='#FBD975', text='Aufgabe erfassen', command=buttonSpeichernClick)
buttonSpeichern.place(x=220, y=100, width=100, height=27)





tkFenster.mainloop()
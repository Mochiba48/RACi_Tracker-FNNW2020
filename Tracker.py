import csv
from tkinter import *
import CSV
import time

startzeitliste = []
endzeitliste = []

def buttonVerarbeitenClick():
    listeAusgewaehlt = listboxAufgaben.curselection()
    itemAusgewaehlt = listeAusgewaehlt[0]
    nameAusgewaehlt = listboxAufgaben.get(itemAusgewaehlt)
    textBegruessung = nameAusgewaehlt
    labelText.config(text=textBegruessung)
    startzeit = time.strftime("%H:%M:%S")
    labelzeit1.config(text=startzeit)
    startzeitliste.append(startzeit)
    print(startzeitliste)

def buttonStoppenClick():
    endzeit = time.strftime("%H:%M:%S")
    labelzeit2.config(text=endzeit)
    endzeitliste.append(endzeit)
    print(endzeitliste)


# Erzeugung des Fensters
tkFenster1 = Tk()
tkFenster1.title('RACi Tracker')
tkFenster1.geometry('400x500')
# Aktivierung des Fensters

#Titel anzeigen
labeltitel = Label(master=tkFenster1, text='Tracking', fg='black', font=('Arial', 16))
labeltitel.place(x=0, y=5, width=350, height=30)


# Uhrzeit anzeigen
uhr = Label(master=tkFenster1)
uhr.place(x=140, y=150)

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



#Aufgabe auswählen
labelAufgaben = Label(master=tkFenster1, text='Aufgabe auswählen')
labelAufgaben.place(x=10, y=40, width=120, height=27)
# Listbox
listboxAufgaben = Listbox(master=tkFenster1, selectmode='browse')
with open('Aufgaben.csv') as f:
    reader =csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data = list(reader)
for i in range(len(data)):
    data1 = data[i]
    data2 = data1[0]
    listboxAufgaben.insert('end',data2)
listboxAufgaben.place(x=140, y=40, width=180, height=50)
# Scroolbar
yScroll = Scrollbar(master=tkFenster1, orient='vertical')
yScroll.place(x=310, y=40, width=10, height=50)
listboxAufgaben.config(yscrollcommand=yScroll.set)
yScroll.config(command=listboxAufgaben.yview)


# Kontrollvariable
text = StringVar()

# Label ausgewählte Aufgabe
labelausaufgabe = Label(master=tkFenster1, text='Ausgewählte Aufgabe')
labelausaufgabe.place(x=10, y=180, width=130, height=27)
labelText = Label(master=tkFenster1, bg='white')
labelText.place(x=140, y=180, width=100, height=27)
labelStartzeit = Label(master=tkFenster1, text='Startzeit')
labelStartzeit.place(x=10, y=210, width=130, height=27)
labelzeit1 = Label(master=tkFenster1, bg='white')
labelzeit1.place(x=140, y=210, width=100, height=27)

labelEndzeit = Label(master=tkFenster1, text='Endzeit')
labelEndzeit.place(x=10, y=270, width=130, height=27)
labelzeit2 = Label(master=tkFenster1, bg='white')
labelzeit2.place(x=140, y=270, width=100, height=27)


# Button verarbeiten
buttonVerarbeiten = Button(master=tkFenster1, text='Aufgabe starten', command=buttonVerarbeitenClick)
buttonVerarbeiten.place(x=140, y=100, width=100, height=27)

buttonStoppen = Button(master=tkFenster1, text='Aufgabe stoppen', command=buttonStoppenClick)
buttonStoppen.place(x=140, y=300, width=100, height=27)


tick()
tkFenster1.mainloop()
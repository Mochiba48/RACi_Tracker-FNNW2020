import csv
from tkinter import *
import CSVintegrator

def AufgabenAuswerten():
    Aufgabenwählen = []
    spezaufgabe = []

    # Erzeugung des Fensters
    tkFenster = Tk()
    tkFenster.title('Auswertung')
    tkFenster.geometry('650x220')
    # Aktivierung des Fensters

    def auswerten1():
        data3 = []
        data5 = []
        with open('Tracker.csv') as f:
            reader = csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            track = list(reader)
        for i in range(len(track)-1):
            track1 = track[i+1]
            track2 = track1[0]
            data3.append(track1)
        listeAufgabe = listboxAusauf.curselection()
        itemAufgabe = listeAufgabe[0]
        nameAufgabe = listboxAusauf.get(itemAufgabe)
        textAufgabe = nameAufgabe
        Aufgabenwählen.append(textAufgabe)
        labelAufgabe.config(text=textAufgabe)
        for k in range(len(data3)):
            data4 = data3[k]
            if Aufgabenwählen[-1] in data4:
                data5.append(data4)
        #print(data5)
        gesamtzeit = 0
        for u in range(len(data5)):
            data6 = data5[u]
            data7 = int(data6[-1])
            gesamtzeit = int(gesamtzeit + data7)
        #print(gesamtzeit)
        if gesamtzeit < 60:
            sec = gesamtzeit
            labelText = Label(master=tkFenster, text=(sec, 'Sekunden'))
            labelText.place(x=220, y=130, width=100, height=27)
        if gesamtzeit >= 60 and gesamtzeit < 3600:
            min = round(gesamtzeit / 60, 2)
            labelText = Label(master=tkFenster, text=(min, 'Minuten'))
            labelText.place(x=220, y=130, width=100, height=27)
        if gesamtzeit >= 3600:
            std = round(gesamtzeit / 3600, 2)
            labelText = Label(master=tkFenster, text=(std, 'Stunden'))
            labelText.place(x=220, y=130, width=100, height=27)
        beschreibung = []
        for y in range(len(spezaufgabe)):
            data8 = spezaufgabe[y]
            #print(data8)
            if Aufgabenwählen[-1] in data8:
                beschreibung = data8[1]
                #print(beschreibung)
                labelBeschreibung.config(text=beschreibung)



        start = []
        ende = []
        arbeitszeit = []
        for m in range(len(track)):
            track3 = track[m]
            #print(track3)
            if Aufgabenwählen[-1] in track3:
                x = 130
                start.append(track3[1])
                ende.append(track3[2])
                labelZeits.config(text=start[0])
                labelZeite.config(text=ende[-1])


    # Titel anzeigen
    labeltitel = Label(master=tkFenster, text='Auswertung der Aufgaben', fg='black', font=('Arial', 16))
    labeltitel.place(x=0, y=5, width=650, height=30)

    # Aufgaben anzeigen
    # Kategorie
    labelAusauf = Label(master=tkFenster, text='Aufgaben')
    labelAusauf.place(x=10, y=40, width=200, height=27)
    # Listbox
    listboxAusauf = Listbox(master=tkFenster, selectmode='browse')
    with open('Aufgaben.csv') as f:
        reader = csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data = list(reader)
    for i in range(len(data)-1):
        data1 = data[i+1]
        spezaufgabe.append(data1)
        data2 = data1[0]
        listboxAusauf.insert('end', data2)
    listboxAusauf.place(x=10, y=65, width=190, height=100)
    # Scroolbar
    yScroll = Scrollbar(master=tkFenster, orient='vertical')
    yScroll.place(x=200, y=65, width=10, height=100)
    listboxAusauf.config(yscrollcommand=yScroll.set)
    yScroll.config(command=listboxAusauf.yview)


    labelAufgabe = Label(master=tkFenster, bg='white')
    labelAufgabe.place(x=220, y=65, width=100, height=27)

    buttonAuswerten = Button(master=tkFenster, text='Auswerten', command=auswerten1)
    buttonAuswerten.place(x=50, y=170, width=100, height=27)

    labelBeschreibung = Label(master=tkFenster, bg='white')
    labelBeschreibung.place(x=340, y=65, width=300, height=27)

    textgeszeit = Label(master=tkFenster, text='Gesamtarbeitszeit')
    textgeszeit.place(x=220, y=100, width=100, height=27)

    textperioden = Label(master=tkFenster, text='Zeitraum, an dem an Aufgabe gearbeitet wurde')
    textperioden.place(x=340, y=100, width=300, height=27)

    textperioden = Label(master=tkFenster, text='Von')
    textperioden.place(x=340, y=130, width=30, height=27)

    labelZeits = Label(master=tkFenster)
    labelZeits.place(x=370, y=130, width=100, height=27)

    textperioden = Label(master=tkFenster, text='bis')
    textperioden.place(x=480, y=130, width=30, height=27)

    labelZeite = Label(master=tkFenster)
    labelZeite.place(x=510, y=130, width=100, height=27)

    tkFenster.mainloop()
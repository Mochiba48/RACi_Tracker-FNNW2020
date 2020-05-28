import csv
from tkinter import *
import CSVintegrator

def Zeitauswertung():
    Aufgabenwählen = []
    spezaufgabe = []
    arbeitszeit = []

    # Erzeugung des Fensters
    tkFenster = Tk()
    tkFenster.title('Auswertung')
    tkFenster.geometry('430x220')
    # Aktivierung des Fensters

    # Titel anzeigen
    labeltitel = Label(master=tkFenster, text='Auswertung nach Datum', fg='black', font=('Arial', 16))
    labeltitel.place(x=0, y=5, width=430, height=30)

    data3 = []
    with open('Tracker.csv') as f:
        reader = csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        track = list(reader)
    for i in range(len(track)):
        track1 = track[i]
        track2 = track1[0]
        data3.append(track1)


    # Benennung
    labelStartdatum = Label(master=tkFenster, text='Startdatum')
    labelStartdatum.place(x=10, y=40, width=200, height=27)
    # Entry
    entryStartdatum = Entry(master=tkFenster, bg='white')
    entryStartdatum.place(x=220, y=40, width=200, height=27)

    labelEnddatum = Label(master=tkFenster, text='Enddatum')
    labelEnddatum.place(x=10, y=70, width=200, height=27)

    entryEnddatum = Entry(master=tkFenster, bg='white')
    entryEnddatum.place(x=220, y=70, width=200, height=27)

    labelArbeitszeit = Label(master=tkFenster, text='geleistete Arbeitszeit:')
    labelArbeitszeit.place(x=10, y=130, width=200, height=27)

    def Auswerten():
        EingabeStart = str(entryStartdatum.get())
        EingabeEnde = str(entryEnddatum.get())
        for k in range(len(data3)):
            data4 = data3[k]
            data5 = data4[1]
            data6 = data5[0:10]
            if EingabeStart <= data6 <= EingabeEnde:
                arbeitszeit.append(data4[-1])
        print(arbeitszeit)
        x = 0
        for m in range(len(arbeitszeit)):
            x = x + int(arbeitszeit[m])
        print(x)
        if x < 60:
            sec = x
            labelText = Label(master=tkFenster, text=(sec, 'Sekunden'))
            labelText.place(x=220, y=130, width=100, height=27)
        if x >= 60 and x < 3600:
            min = round(x / 60, 2)
            labelText = Label(master=tkFenster, text=(min, 'Minuten'))
            labelText.place(x=220, y=130, width=100, height=27)
        if x >= 3600:
            std = round(x / 3600, 2)
            labelText = Label(master=tkFenster, text=(std, 'Stunden'))
            labelText.place(x=220, y=130, width=100, height=27)
        arbeitszeit.clear()
        print(arbeitszeit)



    buttonAuswerten = Button(master=tkFenster, text='Auswerten', command=Auswerten)
    buttonAuswerten.place(x=220, y=100, width=100, height=27)

    tkFenster.mainloop()
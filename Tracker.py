import csv
from tkinter import *
import CSVintegrator
from datetime import time
import time

def TrackerStarten():
    startzeitliste = []
    endzeitliste = []
    aufgabetext = []
    pause = []
    pausenzeit = [0]

    # Erzeugung des Fensters
    tkFenster1 = Tk()
    tkFenster1.title('RACi Tracker')
    tkFenster1.geometry('400x500')
    # Aktivierung des Fensters

    #Titel anzeigen
    labeltitel = Label(master=tkFenster1, text='Tracking', fg='black', font=('Arial', 16))
    labeltitel.place(x=0, y=5, width=350, height=30)

    def buttonStartClick():
        listeAufgabe = listboxAufgaben.curselection()
        itemAufgabe = listeAufgabe[0]
        nameAufgabe = listboxAufgaben.get(itemAufgabe)
        textAufgabe = nameAufgabe
        aufgabetext.append(textAufgabe)
        labelText.config(text=textAufgabe)
        startzeit = time.strftime("%d.%m.%Y %H:%M:%S")
        labelzeit1.config(text=startzeit)
        startzeitliste.append(startzeit)


    def buttonPauseClick():
        startpauset = time.strftime("%H:%M:%S")
        pause.append(startpauset)

        def buttonWeiterClick():
            tkFensterBestätigen.destroy()
            stopppauset = time.strftime("%H:%M:%S")
            pause.append(stopppauset)
            # startzeit
            datens = str(pause[0])
            neush = int(datens[0:2])
            neushs = neush * 3600
            neusm = int(datens[3:5])
            neusms = neusm * 60
            neuss = int(datens[6:8])
            neulist = neushs + neusms + neuss
            # endzeit
            datens = str(pause[-1])
            neueh = int(datens[0:2])
            neuehs = neueh * 3600
            neuem = int(datens[3:5])
            neuems = neuem * 60
            neues = int(datens[6:8])
            neulist1 = neuehs + neuems + neues
            pausenzeit.append(neulist1 - neulist)
        # Neues Fenster öffnen
        tkFensterBestätigen = Toplevel()
        tkFensterBestätigen.title('Information')
        tkFensterBestätigen.geometry('200x80')
        # Label mit der Bestätigung
        labelBestätigen = Label(master=tkFensterBestätigen, text='Pause eingelegt')
        labelBestätigen.place(x=25, y=5, width=150, height=20)
        # Button zum Schließen des Fensters
        buttonOk = Button(master=tkFensterBestätigen, text='Weiter',command=buttonWeiterClick)
        buttonOk.place(x=60, y=35, width=80, height=30)


    def buttonStoppenClick():
        endzeit = time.strftime("%d.%m.%Y %H:%M:%S")
        labelzeit2.config(text=endzeit)
        endzeitliste.append(endzeit)
        zeit = [aufgabetext[-1], startzeitliste[-1], endzeitliste[-1]]

        # auswertung
        datenl = zeit
        # startzeit
        datens = str(datenl[1])
        neush = int(datens[11:13])
        neushs = neush * 3600
        neusm = int(datens[14:16])
        neusms = neusm * 60
        neuss = int(datens[17:19])
        neulist = neushs + neusms + neuss
        # endzeit
        datens = str(datenl[-1])
        neueh = int(datens[11:13])
        neuehs = neueh * 3600
        neuem = int(datens[14:16])
        neuems = neuem * 60
        neues = int(datens[17:19])
        neulist1 = neuehs + neuems + neues
        pausenzeit1 = int(pausenzeit[-1])
        diffs = neulist1 - neulist - pausenzeit1
        zeit.append(diffs)
        #auswertung in tracker.csv speichern
        CSVintegrator.tracker_listeexp(zeit)
        if zeit[-1] < 60:
            sec = zeit[-1]
            labelText = Label(master=tkFenster1, text=('Es wurden', sec, 'Sekunden bei Aufgabe', zeit[0], 'verbucht.'))
            labelText.place(x=0, y=330, width=400, height=27)
        if zeit[-1] >= 60 and zeit[-1] < 3600:
            min = round(zeit[-1] / 60, 2)
            labelText = Label(master=tkFenster1, text=('Es wurden', min, 'Minuten bei Aufgabe', zeit[0], 'verbucht.'))
            labelText.place(x=0, y=330, width=400, height=27)
        if zeit[-1] >= 3600:
            std = round(zeit[-1] / 3600, 2)
            labelText = Label(master=tkFenster1, text=('Es wurden', std, 'Stunden bei Aufgabe', zeit[0], 'verbucht.'))
            labelText.place(x=0, y=330, width=400, height=27)



    #Aufgabe auswählen
    labelAufgaben = Label(master=tkFenster1, text='Aufgabe auswählen')
    labelAufgaben.place(x=10, y=40, width=120, height=27)
    # Listbox
    listboxAufgaben = Listbox(master=tkFenster1, selectmode='browse')
    with open('Aufgaben.csv') as f:
        reader =csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data = list(reader)
    for i in range(len(data)-1):
        data1 = data[i+1]
        data2 = data1[0]
        listboxAufgaben.insert('end',data2)
    listboxAufgaben.place(x=140, y=40, width=180, height=50)
    # Scroolbar
    yScroll = Scrollbar(master=tkFenster1, orient='vertical')
    yScroll.place(x=310, y=40, width=10, height=50)
    listboxAufgaben.config(yscrollcommand=yScroll.set)
    yScroll.config(command=listboxAufgaben.yview)


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
    buttonStarten = Button(master=tkFenster1, text='Aufgabe starten', command=buttonStartClick)
    buttonStarten.place(x=140, y=100, width=100, height=27)

    buttonPause = Button(master=tkFenster1, text='Pause', command=buttonPauseClick)
    buttonPause.place(x=140, y=240, width=100, height=27)

    buttonStoppen = Button(master=tkFenster1, text='Aufgabe stoppen', command=buttonStoppenClick)
    buttonStoppen.place(x=140, y=300, width=100, height=27)



    tkFenster1.mainloop()
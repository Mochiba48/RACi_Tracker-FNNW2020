import time
from tkinter import *

pause = []

pausenzeit = []

# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('RACi Tracker')
tkFenster.geometry('350x500')
# Aktivierung des Fensters


def buttonPauseClick():
    startpauset = time.strftime("%H:%M:%S")
    pause.append(startpauset)
    print(pause)
    def buttonWeiterClick():
        tkFensterBestätigen.destroy()
        stopppauset = time.strftime("%H:%M:%S")
        pause.append(stopppauset)
        print(pause)
        # startzeit
        datens = str(pause[0])
        neush = int(datens[0:2])
        neushs = neush * 3600
        neusm = int(datens[3:5])
        neusms = neusm * 60
        neuss = int(datens[6:8])
        neulist = neushs + neusms + neuss
        # print(neulist)
        # endzeit
        datens = str(pause[-1])
        neueh = int(datens[0:2])
        neuehs = neueh * 3600
        neuem = int(datens[3:5])
        neuems = neuem * 60
        neues = int(datens[6:8])
        neulist1 = neuehs + neuems + neues
        # print(neulist1)
        pausenzeit = neulist1 - neulist
        print(pausenzeit)
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





buttonStoppen = Button(master=tkFenster, text='Aufgabe stoppen', command=buttonPauseClick)
buttonStoppen.place(x=140, y=300, width=100, height=27)


tkFenster.mainloop()
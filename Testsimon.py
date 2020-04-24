import datetime, time
from tkinter import *


# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('RACi Tracker')
tkFenster.geometry('350x500')
# Aktivierung des Fensters


def buttonStart():
    then = datetime.datetime.now() + datetime.timedelta(seconds=5)
    while then > datetime.datetime.now():
        print(time.strftime("%H:%M:%S"))
        time.sleep(1)



buttonStart = Button(master=tkFenster, bg='#FBD975', text='Start', command=buttonStart)
buttonStart.place(x=120, y=140, width=80, height=27)


tkFenster.mainloop()






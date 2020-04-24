import time
from tkinter import *

# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('RACi Tracker')
tkFenster.geometry('350x500')
# Aktivierung des Fensters

def start_counting(label):
    def update(seconds):
        label['text'] = str(seconds)
        label.after(1000, update, seconds + 1)
        print(label['text'])


    update(0)

def buttonStart():
    labelstoppuhr = Label(master=tkFenster, foreground='red')
    labelstoppuhr.place(x=0, y=5, width=350, height=30)
    start_counting(labelstoppuhr)



labelstoppuhr = 5

def buttonStopp():




buttonStart = Button(master=tkFenster, bg='#FBD975', text='Start', command=buttonStart)
buttonStart.place(x=120, y=140, width=80, height=27)

buttonStopp = Button(master=tkFenster, bg='#FBD975', text='Stopp', command=buttonStopp)
buttonStopp.place(x=120, y=240, width=80, height=27)

tkFenster.mainloop()
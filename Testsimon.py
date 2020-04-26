import csv
from datetime import time

#in csv Kategorie importieren:

differenzzeit = []

def arbeitszeit(differenzzeit):
    with open('Tracker.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        daten = list(reader)
        print(daten)
    #letzte erfassung
    datenl = daten[-1]
    #startzeit
    datens = str(datenl[1])
    neush = int(datens[0:2])
    neusm = int(datens[3:5])
    neuss = int(datens[6:8])
    neulist = neush,neusm,neuss
    print(neulist)
    #endzeit
    datens = str(datenl[-1])
    neueh = int(datens[0:2])
    neuem = int(datens[3:5])
    neues = int(datens[6:8])
    neulist = (neueh,neuem,neues)
    print(neulist)
    diffh = neueh - neush
    print(diffh)
    diffm = neuem - neusm
    print(diffm)
    diffs = neues - neuss
    print(diffs)
    differenzzeit = [str(time((diffh), (diffm), (diffs)))]
    #print(differenzzeit)


differenzzeit = arbeitszeit(differenzzeit)

print(differenzzeit)
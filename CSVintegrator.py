import csv
import sys
import os


# CSV finden Aufgaben.csv
def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        datadir = os.path.dirname(r"C:\Users\Acer\Documents\GitHub\RACi_Tracker-FNNW2020\build\exe.win-amd64-3.8")
    return os.path.join(datadir, filename)


find_data_file("Aufgaben.csv")
find_data_file("Kategorie.csv")
find_data_file("Tracker.csv")


# more code...

# in csv aufgabe importieren:
def aufgaben_listeinp(data):
    with open('Aufgaben.csv') as f:
        reader = csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data = list(reader)


# in csv Kategorie importieren:
def kategorie_listeinp(daten):
    with open('Kategorie.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        daten = []
        for line in csv_reader:
            daten.append(line)
        print(daten)


# in csv aufgabe exportieren:
def aufgaben_listeexp(daten):
    with open('Aufgaben.csv', mode='a', newline='') as aufgaben_file:
        aufgaben_writer = csv.writer(aufgaben_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        aufgaben_writer.writerow(daten)


# in csv Kategorie exportieren:
def kategorie_listeexp(daten):
    with open('Kategorie.csv', mode='a', newline='') as kategorie_file:
        kategorie_writer = csv.writer(kategorie_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        kategorie_writer.writerow(daten)


# in csv Tracker exportieren:
def tracker_listeexp(daten):
    with open('Tracker.csv', mode='a', newline='') as tracker_file:
        tracker_writer = csv.writer(tracker_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tracker_writer.writerow(daten)


# in csv alles exportieren (wird alles überschrieben):
def aufgaben_listeexpkompl(daten):
    with open('Aufgaben.csv', mode='w', newline='') as aufgaben_file:
        aufgaben_writer = csv.writer(aufgaben_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        aufgaben_writer.writerow(daten)


daten = ()
aufgaben_listeinp(daten)
print(daten)

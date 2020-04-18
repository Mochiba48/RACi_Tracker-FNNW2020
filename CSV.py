import csv


#in csv importieren:
def aufgaben_listeinp(daten):
    with open('Aufgaben.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)


#in csv aufgabe exportieren:
def aufgaben_listeexp(daten):
    with open('Aufgaben.csv', mode='a', newline='') as aufgaben_file:
        aufgaben_writer = csv.writer(aufgaben_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        aufgaben_writer.writerow(daten)


#in csv alles exportieren (wird alles überschrieben):
def aufgaben_listeexpkompl(daten):
    with open('Aufgaben.csv', mode='w', newline='') as aufgaben_file:
        aufgaben_writer = csv.writer(aufgaben_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        aufgaben_writer.writerow(daten)






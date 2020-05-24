import sys
import tkinter
import csv
from cx_Freeze import setup, Executable

# with open('Aufgaben.csv', 'wb') as csvfile:
#     filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#
# with open('Kategorie.csv', 'wb') as csvfile:
#     filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#
# with open('Tracker.csv', 'wb') as csvfile:
#     filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

build_exe_options = {"packages": ["os"], "excludes": [tkinter]}
base = None
if sys.platform == "win32":
    base = "Win32GUI"

if sys.platform == "win64":
    base = "Win64GUI"

setup(  name = "RACITracker",
        version = 0.1,
        description = "by Simon Fluri, Daniel Thran",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Hauptfenster.py", base=base)])



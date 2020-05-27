import os
import sys
import tkinter
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\Acer\AppData\Local\Programs\Python\Python38\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Acer\AppData\Local\Programs\Python\Python38\tcl\tk8.6'

sys.argv.append("build")



build_exe_options = {"packages": ["os"], "excludes": [tkinter],
                     "include_files": ["RACI-Tracker.gif", "Aufgaben.csv",
                                       "Kategorie.csv", "Tracker.csv",
                                       r'C:\Users\Acer\AppData\Local\Programs\Python\Python38\DLLs\tcl86t.dll', r'C:\Users\Acer\AppData\Local\Programs\Python\Python38\DLLs\tk86t.dll']}
base = None
if sys.platform == "win32":
    base = "Win32GUI"

if sys.platform == "win64":
    base = "Win64GUI"

setup(  name = "RACITracker",
        version = 0.1,
        description = "by Simon Fluri, Daniel Thran",
        options = {"build_exe": build_exe_options},
        executables = [Executable("RACI-Tracker.py", base=base)])


#CSV finden Aufgaben.csv
def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        datadir = os.path.dirname(r"C:\Users\Acer\Documents\GitHub\RACi_Tracker-FNNW2020")
    return os.path.join(datadir, filename)

#CSV importieren
# find_data_file("Aufgaben.csv")
# find_data_file("Kategorie.csv")
# find_data_file("Tracker.csv")
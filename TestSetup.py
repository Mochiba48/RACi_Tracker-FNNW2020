import os
import sys
import tkinter
from cx_Freeze import setup, Executable

sys.argv.append("build")
#sys.argv.append("bdist_mac")

build_exe_options = {"packages": ["os", tkinter],
                     "include_files": ["RACI-Tracker.gif", "Aufgaben.csv",
                                       "Kategorie.csv", "Tracker.csv"]}


base = None

executables = [
    Executable('RACI-Tracker.py', base=base)
]

setup(name="RACITracker",
      version=0.1,
      description="by Simon Fluri, Daniel Thran",
      options={"build_exe": build_exe_options},
      executables=executables)


def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(r"C:\Users\Acer\Documents\GitHub\RACi_Tracker-FNNW2020")
    return os.path.join(datadir, filename)
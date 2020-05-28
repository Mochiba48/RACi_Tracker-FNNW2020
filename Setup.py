import os
import sys
from tkinter import *
from cx_Freeze import setup, Executable


os.environ['TCL_LIBRARY'] = r'C:\Users\Acer\AppData\Local\Programs\Python\Python38\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Acer\AppData\Local\Programs\Python\Python38\tcl\tk8.6'

sys.argv.append("build")

build_exe_options = {"packages": ["os", "sys"], "includes": ["tkinter"],
                     "include_files": ["RACI-Tracker.gif", "Aufgaben.csv", "Kategorie.csv", "Tracker.csv",
                                       r'C:\Users\Acer\AppData\Local\Programs\Python\Python38\DLLs\tcl86t.dll',
                                       r'C:\Users\Acer\AppData\Local\Programs\Python\Python38\DLLs\tk86t.dll']}
base = None
if sys.platform == "win32":
    base = "Win32GUI"

if sys.platform == "win64":
    base = "Win64GUI"

setup(name="RACITracker",
      version=0.1,
      description="by Simon Fluri, Daniel Thran",
      options={"build_exe": build_exe_options},
      # icon="RaciTracker.ico",
      executables=[
          Executable(
            "RACI-Tracker.py",
            base=base)])

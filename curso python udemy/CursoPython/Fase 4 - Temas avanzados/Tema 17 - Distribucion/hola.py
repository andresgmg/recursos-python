import sys
import os
from tkinter import *

def resource_path(relative_path):
    """ Get absolute path resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = Tk()
imagen = PhotoImage(file=resource_path("src/facelad.png"))
Label(image=imagen).pack()
root.mainloop()
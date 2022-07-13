from os import mkdir, chdir, listdir, path
from os.path import join, isdir
from pprint import pp
import tkinter
from tkinter import MOVETO
from tkinter.filedialog import askdirectory
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    #CoDy's folder
    destPath = "c:\\Program Files (x86)\\CoDy"

    #Create destination folder if it doesn't exist
    exists = path.exists(destPath)
    if exists == False:
        mkdir(destPath)

    #Ask user to select a source folder
    srcPath = askdirectory(title = 'Select Folder')

    #Closes Tk window
    tkinter.tk().withdraw()

    #Working directory
    chdir(srcPath)

    edirs = [join(srcPath, x) for x in listdir() if isdir(x)]
    pp(edirs)
    for d in edirs:
        for f in listdir(d):
            if f.endswith('.mp4'):
                pp(f)
                MOVETO(join(d, f), d + '.mp4')
                pp(d)
else:
    #Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
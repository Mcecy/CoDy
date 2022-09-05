import os
from tkinter.filedialog import askdirectory
from file import movefile

#Ask user to select a source folder
src_path = askdirectory(title = 'Select Folder')

#CoDy's folder
dest_path = f"{src_path}\\CoDy"

#Create destination folder if it doesn't exist
exists = os.path.exists(dest_path)
if not exists:
    os.mkdir(dest_path)

try:
    print("Starting the tool...")

    movefile(src_path, dest_path)

    print("Finished.")
except FileNotFoundError as e:
    print(f"Error: {e}")

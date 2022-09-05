import os
from tkinter.filedialog import askdirectory
from file import movefile

#CoDy's folder
dest_path = "c:\\CoDy"

#Create destination folder if it doesn't exist
exists = os.path.exists(dest_path)
if not exists:
    os.mkdir(dest_path)

#Ask user to select a source folder
src_path = askdirectory(title = 'Select Folder')

while True:
    file_type = input("Choose a file type to work with(pdf/mp4/rtf/docx/exe) or exit: ")

    if file_type.lower() == 'exit':
        quest = input("Want to choose another folder?(y/n) ")

        if quest.lower() == 'n':
            break
        elif quest.lower() == 'y':
            src_path = askdirectory(title = 'Select Folder')
        else:
            print("Invalid response.")
    elif file_type.lower() == 'pdf' or 'mp4' or 'rtf' or 'docx' or 'exe':
        movefile(src_path, dest_path, file_type)
    else:
        print("Invalid response.")


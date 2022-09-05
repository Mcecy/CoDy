import os
from shutil import move, copy

def movefile(src_path, dest_path):
    for directory, subfolders, files in os.walk(src_path):
        for file in files:

            *_, ext = os.path.splitext(f"{src_path}/{file}")
            ext = list(ext)

            if ext:
                ext.pop(0)
                ext = "".join(ext)
                file_path = os.path.abspath(file)

                if os.path.exists(file_path):
                    if not os.path.exists(f"{dest_path}/{ext}"):
                        os.mkdir(f"{dest_path}/{ext.upper()}")
                        copy(file_path, f"{dest_path}/{ext}/{file}")
                    else:
                        copy(file_path, f"{dest_path}/{ext}/{file}")
                else:
                    continue
            else:
                break
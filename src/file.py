import os
from shutil import move

def movefile(src_path, dest_path, file_type):
    for diretorio, subpastas, arquivos in os.walk(src_path):
        for arquivo in arquivos:
            if arquivo.endswith(f".{file_type}"):
                if not os.path.exists(f"{dest_path}/{file_type}"):
                    os.mkdir(f"{dest_path}/{file_type.upper()}")
                    move(f"{src_path}/{arquivo}", f"{dest_path}/{file_type}/{arquivo}")
                else:
                    move(f"{src_path}/{arquivo}", f"{dest_path}/{file_type}/{arquivo}")
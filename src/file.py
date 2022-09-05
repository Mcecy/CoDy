import os
from shutil import move

def movefile(src_path, dest_path):
    for diretorio, subpastas, arquivos in os.walk(src_path):
        for diret in diretorio:
            for subpasta in subpastas:
                for arquivo in arquivos:
                    *_, ext = os.path.splitext(f"{diret}/{subpasta}/{arquivo}")

                    if not os.path.exists(f"{dest_path}/{ext}"):
                        os.mkdir(f"{dest_path}/{ext.upper()}")
                        move(f"{diret}/{subpasta}/{arquivo}", f"{dest_path}/{ext}/{arquivo}")
                    else:
                        move(f"{src_path}/{arquivo}", f"{dest_path}/{ext}/{arquivo}")
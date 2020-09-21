#! python3
# deleteFileInutil.py - Procura arquivos ou pastas que tenham um tamanho maior que 100 MB.

import os, send2trash

def deleteFileInutil(folder):

    folder = os.path.abspath(folder)
    print(folder)

    for foldername, subfolders, filenames in os.walk(folder):

        for filename in filenames:
            print('File inside ' + foldername + ':' + filename)
            if os.path.getsize(filename) >= 104857600: # 100 MB é 104.857.600 bytes
                send2trash.send2trash(filename)
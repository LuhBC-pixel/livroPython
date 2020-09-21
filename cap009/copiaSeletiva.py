#! python3
# copiaSeletiva.py - Percorre uma árvore de diretórios e procura arquivos com determinada extensão
# (.pdf ou .jpg) e copia esses arquivos do local ao uma nova pasta.

import os, shutil

def copiaSeletiva(arquivo):

    file = os.path.abspath(arquivo)

    for foldername, subfolders, filenames in os.walk(file):
        for filename in filenames:
            if filename.endswith('.pdf') or filename.endswith('.jpg'):
                shutil.copy(filename, 'C:\\Desktop')
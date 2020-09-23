#! python3
# mapIt.py - Inicia um mapa no navegador usando um endereço da
# linha de comando ou do clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Obtém o endereço da linha de comando.
    address = ' '.join(sys.argv[1:])
else:
    # Obtém o endereço do clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
#! python3
# luck.py - Abre vários resultados de pesquisa no Google.

import requests, sys, webbrowser, bs4

search = ' '.join(sys.argv[1:])

print('Googling...') # exibe um texto enquanto faz download da página do Google
res = requests.get('https://google.com.br/search?q=' + search)
res.raise_for_status()

# Obtém os links dos principais resultados da pesquisa.
soup = bs4.BeautifulSoup(res.text)

# Abre uma aba do navegador para cada resultado.
# linkElems = soup.select('.r a') não esta dando certo, então segundo o site
# https://stackoverflow.com/questions/56664934/soup-select-r-a-in-fhttps-google-com-searchq-query-brings-back-empty
linkElems = soup.select('div#main > div > div > div > a')
print(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

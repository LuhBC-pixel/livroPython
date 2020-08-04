spam = ['apples', 'bananas', 'tofu', 'cats']

def listaString(lista):
    string = ''
    for i in range(len(lista)):
        if i >= (len(lista) - 1):
            string += f'{lista[i]}'
        else:
            string += f'{lista[i]} and '
    return string

print(listaString(spam))
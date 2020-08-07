def printTables(listaString):
    colWidth = [0] * len(listaString)

    for i in range(len(listaString)):
        maior = 0
        for j in range(len(listaString[i])):
            if len(listaString[i][j]) > maior:
                maior = len(listaString[i][j])
                letra = listaString[i][j]
        colWidth[i] = letra

    stringLonga = max(colWidth)
    tamanho = len(stringLonga)

    for x in range(len(listaString[0])):
        for j in range(len(listaString)):
            if j >= len(listaString) - 1:
                print(str(listaString[j][x]).rjust(tamanho))
            else:
                print(str(listaString[j][x]).rjust(tamanho), end=' ')

tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]
printTables(tableData)
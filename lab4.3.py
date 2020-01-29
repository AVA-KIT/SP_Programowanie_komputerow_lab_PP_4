lista_1 = [1, 2, 3, 4, 5, 9]
lista_2 = [5, 6, 7, 3, 1, 8]
lista_3 = []
for i in lista_1:
    if i not in lista_2:
        lista_3.append(i)
for i in lista_2:
    if i not in lista_1:
        lista_3.append(i)

print(lista_3)
pesel = input('Podaj PESEL: ')
dl = len(pesel)

while pesel.isdigit() == False:
    pesel = input('Podaj poprawny PESEL: ')
    if dl != 11:
        pesel = input('Podaj poprawny PESEL: ')
    else:
        break


print(pesel)
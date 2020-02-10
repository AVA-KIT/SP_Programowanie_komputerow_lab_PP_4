import sys
pesel = input('Podaj PESEL: ')

while len(pesel) != 11:
    pesel = input('PESEL powinien posiadać 11 cyfr. Podaj poprawny PESEL: ')

PESEL = []
NZNAKI = []
for i in pesel:
    if i.isdigit() == True:
        PESEL.append(int(i))
    else:
        NZNAKI.append(i)

def czyCyfry(znaki):
    if  len(znaki) != 0:
        print('Niedozwolone znaki: ', znaki, '. Zacznij od początku')
        sys.exit(0)

czyCyfry(NZNAKI)

def okresPlec(plec):
    if plec % 2 != 0:
        print('Jesteś mężczyzną')
    else:
        print('Jesteś kobietą')

okresPlec(PESEL[9])
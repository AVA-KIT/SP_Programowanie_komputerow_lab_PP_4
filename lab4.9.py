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

def czyPoprawny(PESEL):
    suma = PESEL[0] + 3*PESEL[1] + 7*PESEL[2] + 9*PESEL[3] + PESEL[4] + 3*PESEL[5] + 7*PESEL[6] + 9*PESEL[7] + PESEL[8] + 3*PESEL[9] + PESEL[10]
    SUMA = list(str(suma))
    if int(SUMA[-1]) == 0:
        print('Twój PESEL jest poprawny')
    else:
        print('Twój PESEL jest niepoprawny')

czyPoprawny(PESEL)
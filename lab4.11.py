# Wyznacznie NWD (Największy Wspólny Dzielnik) i NWW (Najmniejszą Wspólną Wielokrotność)
# przy pomocy algorytmu Euklidesa w wersji z dzieleniem modulo
print()
print('Wyznaczamy NWD i NWW dla dwóch liczb naturalnych')
print()

a = int(input('Podaj pierwszą liczbę naturalną: '))

while a < 0:
    print('To nie jest liczba naturalna') 
    a = int(input('Podaj pierwszą liczbę naturalną: '))

b = int(input('Podaj drugą liczbę naturalną: '))
while b < 0:
    print('To nie jest liczba naturalna') 
    b = int(input('Podaj drugą liczbę naturalną: '))

print()

c = 0
d = a
e = b

while a % b != 0:
    c = a % b
    a = b
    b = c
else:
    print('NWD liczb: ',d,' i ',e, 'to: ',b)

f = (d * e) / b

print('NWW liczb: ',d,' i ',e, 'to: ',int(f))
print()


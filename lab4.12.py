#Program oblicza N-ty (podany przez użytkownika) wyraz ciągu Fibonacciego
print()
n = int(input("Podaj numer wyrazu ciągu do wyliczenia: "))

def Fib(n):
    if n < 0:
        print('Nie można policzyć {} wyrazu ciągu Fibonacciego'.format(n))
    elif n == 0:
        print(n,' wyraz ciągu to: 0')
    elif n == 1:
        print(n,' wyraz ciągu to: 1')
    else:
        el1 = el2 = 1
        suma = 0
        for i in range(3,n+1):
            suma = el1 + el2
            el1, el2 = el2, suma
        return suma
print()
print(n,' wyraz ciągu to: ',Fib(n))
print()
import random
print("Losujemy 5 liczb z podanego zakresu")
a = float(input('Podaj początek zakresu: ')) 
b = float(input('Podaj koniec zakresu: '))
i = 0
for i in range(0,5,1):
    print(random.uniform(a,b))

import random
print("Losujemy 5 liczb z podanego zakresu")
a = float(input('Podaj początek zakresu: ')) 
b = float(input('Podaj koniec zakresu: '))
i = 0
w =[]

for i in range(0,5,1):
    w.append(round(random.uniform(a,b),3))

for j in w:
    print(j)

v = input('Wypisz pierwszy ciąg znaków: ')
x = input('Wypisz drugi ciąg znaków: ')

dict1 = {}
dict2 = {}
for i in v:
    dict1[i] = [v.count(i)]
for j in x:
    dict2[j] = [v.count(j)]

def czyAnagram(d1, d2):
    if d1 == d2:
        print(True)
        return True
    else:
        print(False)
        return False

czyAnagram(dict1, dict2)

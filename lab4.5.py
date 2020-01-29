v = input('Wypisz dowolny ciąg znaków: ')

def czyPalindrom(i):
    if i == i[::-1]:
        print(True)
        return True
    else:
        print(False)
        return False

czyPalindrom(v)

    
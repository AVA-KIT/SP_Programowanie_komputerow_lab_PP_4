email = input('Podaj adres email: ')
k = ['.pl','.com','.org','.edu','.net']
def czyEmail(email):
    for i in k:
        if email.endswith(i) == False and i != k[-1]:
           continue
        elif email.endswith(i) == True and '@' in email and email.index('@') != 0:
           print ('Twój email jest poprawny')
           break
        else:
            print ('To nie jest adres email')
            break
         
czyEmail(email)



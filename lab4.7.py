email = 'ala@ala.pl'

def czyEmail(email):
    k = ['.pl','.com','.org','.edu',]
    for i in k:
        if email.endswith(i) and '@' in email:
           return True
           print ('tak')
        else:
           return False
            
        
czyEmail(email)



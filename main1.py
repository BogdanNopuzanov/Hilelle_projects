pershe_chislo=float(input('Pershe chislo: '))
deistvie=str(input('vvedite + - * /: '))
druge_chislo=float(input('Druge chislo: '))

if deistvie=='+':
    rezultat= pershe_chislo+druge_chislo
elif deistvie=='-':
    rezultat= pershe_chislo-druge_chislo
elif deistvie=='*':
    rezultat= pershe_chislo*druge_chislo
elif deistvie=='/':
    if druge_chislo==0:
        rezultat= 0
        print('ne delim na 0')
    else:
        rezultat= pershe_chislo/druge_chislo

print(pershe_chislo,deistvie,druge_chislo,rezultat)
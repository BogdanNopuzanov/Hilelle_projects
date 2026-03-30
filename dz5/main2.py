while True:
    num1=float(input('pershe chislo:'))
    action=str(input('deistvie - + * /:'))
    num2=float(input('druge chislo:'))
    rezultat=''
    if action=='/':
     if num2==0:
            rezultat='nelza tak'
     else:
          rezultat=str(num1/num2)
    elif action=='*':
        rezultat = str(num1 * num2)
    elif action=='-':
        rezultat = str(num1 - num2)
    elif action=='+':
        rezultat = str(num1 + num2)
    else: rezultat ='ne ponal \n'
    print(rezultat)
    rezultat = str(input('prodolzhim?(yes,y):'))
    if rezultat.lower() not in ('yes','y'):
        break
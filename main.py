def main1():
    user_input=float(input())
    print(user_input**2)
def main2():
    user_input1=int(input())
    user_input2 = int(input())
    user_input3 = int(input())
    print((user_input1+user_input2+user_input3)//3)
def main3():
    user_input1=int(input('кількість хвилин:'))
    godini, hvilini = divmod(user_input1, 60)
    print('hvilini=')
    print(hvilini)
    print('godini=')
    print(godini)
def main4():
    stoimost=int(input('ціну товару:'))
    znizhka = int(input('розмір знижки:'))
    resultat = stoimost-((stoimost*znizhka)/100)
    print(resultat)
def main5():
    user_input1=int(input(':'))
    resultat = user_input1%10
    print(resultat)
def main6():
    dovzhina = int(input('dovzhina:'))
    shirina = int(input('shirina:'))
    resultat = dovzhina*2 + shirina*2
    print(resultat)
def main7():
    user_input1=int(input('chetireznachne chislo:'))
    print(user_input1 // 1000)
    print((user_input1 % 1000) // 100)
    print(user_input1 % 100 // 10)
    print(user_input1%10)
def main8():
    user_input1=int(input('chetireznachne chislo:'))
    print(user_input1 // 1000)
    print((user_input1 % 1000) // 100)
    print(user_input1 % 100 // 10)
    print(user_input1%10)



main7()
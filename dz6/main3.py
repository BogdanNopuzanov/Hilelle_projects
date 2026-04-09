# Получаем число от пользователя
number = int(input("Введіть ціле число: "))

while number > 9:
    skvoznoe = 1

    for digit in str(number):
        skvoznoe *= int(digit)

    number = skvoznoe

print(number)
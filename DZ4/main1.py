
num = [1, 0, 13, 0, 0, 0, 5]

for i in range(len(num) - 1, -1, -1):
    if num[i] == 0:
        num.pop(i)
        num.append(0)

print(num)

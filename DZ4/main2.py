list_1 = [0, 1, 7, 2, 4, 8]
num = [list_1[i] for i in range(len(list_1)) if i % 2 == 0 ]

print(num)
print(sum(num)*list_1[-1])
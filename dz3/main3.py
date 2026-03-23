list_1 =[1, 2, 3, 4, 5]
print(list_1)
#print(len(list_1)/2)
size=len(list_1)//2+len(list_1)%2 #не хотел использовать if

list_2=list_1[:size]
print(list_2)
list_3=list_1[size:]
print(list_3)
#print(size)
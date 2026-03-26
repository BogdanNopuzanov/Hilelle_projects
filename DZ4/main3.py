import random
def main1():
    list_1=[]
    for i in range(random.randint(3, 10)):
        list_1.append(random.randint(3, 10))
    print(list_1)
    print(list_1[0], list_1[2], list_1[-2])
main1()
a = int(input("Please input size of lesenka: "))
list = [i for i in range(1, a+1)]
for i in range(1, a+1):
    print(*list, sep='')
    list.remove(max(list))
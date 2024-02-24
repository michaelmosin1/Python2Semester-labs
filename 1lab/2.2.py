a = int(input("Please input size of lesenka: "))
list = [i for i in range(2, a+1)]
stroka_nach = ''
for j in list: stroka_nach += str(j)
for i in range(a, 0, -1):
    stroka = ''
    for j in list: stroka += str(j)
    print(*reversed(list), '1', *list, sep='')
    print(' '*(len(stroka_nach)-len(stroka)+len(str(i))), end='')
    if i != 1: list.remove(i)
print('\n')

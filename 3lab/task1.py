stroka_old = str(input("Please input string: "))
stroka_new = ''
for index in range(len(stroka_old)):
    symbol = stroka_old[index]
    count = stroka_old.count(symbol)
    if not(symbol+str(count) in stroka_new):
        stroka_new += symbol
        if count != 1:
            stroka_new += str(count)
print(stroka_new)

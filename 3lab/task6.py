stroka = str(input("Please input string: "))
stroka = stroka.title()
for i in stroka:
    if i.islower() or i == ' ': stroka = stroka.replace(i, '', 1)
print(stroka)

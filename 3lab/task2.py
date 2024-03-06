stroka_old = str(input("Please input string: "))
stroka_new = ''
for i in range(len(stroka_old)):
    if not stroka_old[i].isdigit():
        count = ''
        j = i + 1
        while j < len(stroka_old) and stroka_old[j].isdigit():
            count += str(stroka_old[j])
            j += 1
        if count == '': count = 1
        if not (stroka_old[i] in stroka_new):
            stroka_new += (stroka_old[i]*int(count))
print(stroka_new)

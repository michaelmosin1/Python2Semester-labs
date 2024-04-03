stroka = list(input("Please input your string:\n").split())
_dict = dict()
for i in stroka:
    _dict[i] = stroka.count(i)
sorted_dict = sorted(_dict.items(), key=lambda item: (item[1], item[0]))
for i in sorted_dict:
    print(i[0])

array = ['stroka1', 'stroka2', 'stroka2', 'stroka1' ,'stroka3', 'stroka4']
dictionary = {i:array.count(i) for i in array}
print(*list(dictionary.values()))
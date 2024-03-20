from collections import defaultdict
n = int(input())
_dict = defaultdict(list)
for i in range(n):
    client, product, quantity = input().split()
    _dict[client].append(product+' '+quantity)
for i in list(_dict.keys()):
    print(f'Покупатель {i}:')
    for j in _dict[i]:
        print(j)

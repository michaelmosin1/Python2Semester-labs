n = int(input())
prev_str = [1]
for i in range(n):
    print(' '*(n-i), end='')
    print(*prev_str)
    new_str = prev_str.copy()
    new_str.append(1)
    for a in range(1, len(new_str)-1):
        new_str[a] = prev_str[a]+prev_str[a-1]
    prev_str = new_str

words = input().split()
for i in range(len(words)):
    count = 0
    for j in range(i):
        if words[j] == words[i]:
            count += 1
    print(count, end=' ')
print()

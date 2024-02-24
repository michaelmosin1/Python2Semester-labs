import copy


def PrintTriangleH(howMany):
    prev1_str = [' *  ']
    invicibleSpace = ['    ']
    if (howMany%2 == 0) or (howMany == 1):
        for i in range(howMany):
            print(*prev1_str, end='')
    else:
        print(*prev1_str, end='')
        for i in range(howMany-2):
            print(*invicibleSpace, end='')
        print(*prev1_str, end='')
    print()

def PrintTriangleL(howMany):
    prev2_str = ['* * ']
    invicibleSpace = ['    ']
    if (howMany%2 == 0) or (howMany == 1):
        for i in range(howMany):
            print(*prev2_str, end='')
    else:
        print(*prev2_str, end='')
        for i in range(howMany-2):
            print(*invicibleSpace, end='')
        print(*prev2_str, end='')
    print()


n = int(input())
prev_str = [1]
for i in range(n):
    print(' '*(n-i), end='')
    print(*prev_str)
    new_str = copy.copy(prev_str)
    new_str.append(1)
    for a in range(1, len(new_str)-1):
        new_str[a] = prev_str[a]+prev_str[a-1]
    prev_str = new_str


for i in range(n):
    print('  '*(n-i), end='')
    PrintTriangleH(i+1)
    print('  '*(n-i), end='')
    PrintTriangleL(i+1)
print()
        

    
    
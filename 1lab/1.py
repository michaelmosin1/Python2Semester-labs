a = int(input("Please input number A:   "))
b = int(input("PLease input number B:   "))
c = int(input("PLease input number C:   "))
if (a == b) and (b == c): print("All numbers are equal ")
if (a == b): 
    if (a > c):
        print("a == b ")
        max_number = a
        min_number = c
    else:
        max_number = c
        min_number = a
elif (a == c): 
    if (a > b):
        print("a == c ")
        max_number = a
        min_number = b
    else:
        max_number = b
        min_number = a
elif (c == b): 
    if (c > a):
        print("b == c ")
        max_number = b
        min_number = a
    else:
        max_number = a
        min_number = b
else:
    if (a > b) and (a > c):
        max_number = a
        if (b > c): min_number = c
        else: min_number = b
    elif (b > a) and (b > c):
        max_number = b
        if (a > c): min_number = c
        else: min_number = a
    elif (c > a) and (c > b):
        max_number = c
        if (a > b): min_number = b
        else: min_number = a
print("Max number is ", max_number, "\nMin number is ", min_number)

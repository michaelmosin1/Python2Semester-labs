mat = [
[1, 2, 3],
[2, 4, 6],
[3, 6, 9]        
]
proportionals = {}
for i in range(2):
    for j in range(i+1, 3):
        coefficient = mat[j][0]/mat[i][0]
        are_proportional = True
        for k in range(1, 3):
            if mat[j][k]/mat[i][k] != coefficient:
                are_proportional = False
                break
        if are_proportional:
            proportionals[i+1] = 1
            proportionals[j+1] = 1
print(*list(proportionals.keys()), "columns are proportional")

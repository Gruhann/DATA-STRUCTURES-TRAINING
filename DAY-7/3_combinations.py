b = []

def bc(l, a, i):
    if len(a) == 3:
        b.append(a[:])  
        return
    for j in range(i, len(l)):
        a.append(l[j])
        bc(l, a, j + 1)
        a.pop()  
    return b

l = [1, 2, 3, 4, 5, 6, 7]
print(bc(l, [], 0))

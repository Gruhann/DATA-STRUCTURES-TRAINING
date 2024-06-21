# max no of queens in given matrix

def is_safe(row, col, a, n, m):
    if a[row][col] ==99:
        return False
    for i in range(col):# Check the same row on the left side
        if a[row][i] == 1:
            return False
    for i in range(row):# Check the same column above
        if a[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):# Check the upper left diagonal
        if a[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):# Check the lower left diagonal
        if a[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, m, 1)):# Check the upper right diagonal
        if a[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, m, 1)):# Check the lower right diagonal
        if a[i][j] == 1:
            return False
    
    return True

def nqueens(a, col, n, m):
    if col >= m:
        return True
    for i in range(n):
        if is_safe(i, col, a, n, m):
            a[i][col] = 1
            if nqueens(a, col + 1, n, m):
                return True
            a[i][col] = 0
    return False

n = int(input())
m = int(input())

a = [[0 for _ in range(m)] for _ in range(n)]
a[4][4]=99
c=0
if nqueens(a, 0, n, m):
    for row in a:
        c+=row.count(1)
        print(row)
    print(c)
else:
    print("\nNo solution exists")

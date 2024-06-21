def is_safe(row,col,a):
    for i in range(col):
        if a[row][i]==1:
            return False
    
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):#upper left diagonal
        if a[i][j]==1:
            return False
    
    for i,j in zip(range(row,len(a),1),range(col,-1,-1)):#lower left diagonal
        if a[i][j]==1:
            return False
    return True

def nqueens(a,col):
    if col>=len(a):
        return True
    for i in range(len(a)):
        if is_safe(i,col,a):
            a[i][col]=1
            if nqueens(a,col+1):
                return True
            a[i][col]=0
    return False
n=8
a=[[0 for i in range(n)] for i in range(n)]
for i in a:print(i)
nqueens(a,0)
print()
for row in a:
    print(row)
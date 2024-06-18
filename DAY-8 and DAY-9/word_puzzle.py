n = int(input())
m = []
for i in range(n):
    m.append(list(map(str, input().split())))

w= (input())
c=0
def check(i,j,k,t):
    if k==len(w):
        return 1
    if i<0 or j<0 or i>=n or j>=n or m[i][j]!=w[k]:
        return 
    if m[i][j]==w[k]:
        m[i][j]=0
    if k!=len(w):
        t=check(i+1, j,k+1,t)
        t=check(i-1, j,k+1,t)
        t=check(i, j+1,k+1,t)
        t=check(i, j-1,k+1,t)
    return t

for i in range(n):
    for j in range(n):
        if m[i][j]==w[0]:
            c=check(i,j,1,0)
            if c==1:
                print("found")
                break
if c==0:
    print("not found")
# check(0,0,0)

'''
leetcode problem 79
'''
'''
w o e s
o r a w
q d o q
m m s u

'''
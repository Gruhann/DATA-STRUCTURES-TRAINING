#counting total paths in a given matrix from start to end
'''
row = 3
col = 4
mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
l = []
def fun(i,j,c):
    if j < 0 or j == col or i < 0 or i == row or (i,j) in l:
        return c
    if i == row-1 and j == col-1:
        l.append((i,j))
        c = c+1
        print(l)
        l.pop()
        return c 
    l.append((i,j))
    c = fun(i+1,j,c)
    c = fun(i-1,j,c)
    c = fun(i,j+1,c)
    c = fun(i,j-1,c)
    l.pop()
    return c 
print(fun(0,0,0))
'''
#with an obstacle in middle of the path
row = 3
col = 4
obs = (0,2)
l = []
def fun(i,j,c,obs):
    if j < 0 or j == col or i < 0 or i == row or (i,j) in l or (i,j) == obs:
        return c
    if i == row-1 and j == col-1:
        l.append((i,j))
        c = c+1
        print(l)
        l.pop()
        return c 
    l.append((i,j))
    c = fun(i+1,j,c,obs)
    c = fun(i-1,j,c,obs)
    c = fun(i,j+1,c,obs)
    c = fun(i,j-1,c,obs)
    l.pop()
    return c 
print(fun(0,0,0,obs))
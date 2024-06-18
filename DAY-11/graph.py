
d={5:[(7,3),(3,2)],
   7:[(5,3),(4,6),(3,1)],
   4:[(7,6),(8,5),(2,1)],
   3:[(5,2),(7,1),(8,4)],
   8:[(3,4),(4,5),(2,4)],
   2:[(4,1),(8,4)]}

d1={5:[(7),(3)],
   7:[(5),(4),(3)],
   4:[(7),(8),(2)],
   3:[(5),(7),(8)],
   8:[(3),(4),(2)],
   2:[(4),(8)]}
# def spanning_tree(i,v):
#     print(i,end=" ")
#     v.append(i)
#     for j in d1[i]:
#         if j not in v:
#             spanning_tree(j,v)

def all_paths_tree(x,v):
    v.append(x)
    if x==2:
        print(v)
        v.pop()
        return
    for i in d1[x]:
        if i not in v:
            all_paths_tree(i,v)
    v.pop()

def cost_spanning_tree(x,v,c):
    v.append(x)
    if x==2:
        print(v,c)
        v.pop()
        return
    for i,j in d[x]:
        if i not in v:
            cost_spanning_tree(i,v,c+j)
    v.pop() 
def min_cost_of_spanning_tree(x,e,v,c,m):
    v.append(x)
    if x==e:
        if c<m:
            m=c
        v.pop()
        # print(m)
        return m
    for i,j in d[x]:
        if i not in v:
           m= min_cost_of_spanning_tree(i,e,v,c+j,m)
    v.pop()
    return m

def min_cost_spanning_tree(x,v,c,m,l):
    v.append(x)
    if x==2:
        if c==m:
            l.append(v[:])#append other spanning trees of same length
        if c<m:
            m=c
            l=v.copy()
        v.pop()
        return m,l
    for i,j in d[x]:
        if i not in v:
           m,l= min_cost_spanning_tree(i,v,c+j,m,l)
    v.pop()
    return m,l
# spanning_tree(5,[])
# print(d1.keys())
# all_paths_tree(5,[]) 
# cost_spanning_tree(5,[],0) 
for i in d.keys():
    print(i,min_cost_of_spanning_tree(5,i,[],0,10000)) 
# print(min_cost_spanning_tree(5,[],0,1000000,[])) 



 

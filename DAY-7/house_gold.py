l=list(map(int,input().split(" ")))
def maxp(l,s):
    if len(l)==0:
        print(l,s)
        return 0
    if len(l)==1:
        print(l,s)
        return l[0]
    if len(l)==2:
        print(l,s)
        return max(l)
    ls=l[0]+maxp(l[2:],s+l[0])
    print(l,s)
    rs=l[1]+maxp(l[3:],s+l[1])
    return max(ls,rs)
print(maxp(l,0))
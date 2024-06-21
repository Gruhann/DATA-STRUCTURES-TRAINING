l=[3,5,9,6,8,10]
l=[3,5,10,9,2,3]
m=0
res=[]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
        res.append(l[i])
l=l[::-1]
m=0
res2=[]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
        res2.append(l[i])
print(res,res2)


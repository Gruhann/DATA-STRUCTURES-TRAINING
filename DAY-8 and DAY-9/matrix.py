# l=list(map(int,input().split(" ")))
# res=[]
# c=0
# while c!=len(l):
#     a=[]
#     for i in range(len(l)):
#         if str(l[i]).isdigit():
#             if l[i] not in a:
#                 c+=1
#                 a.append(l[i])
#                 l[i]="a"
#     res.append(a)
# print(res)

a=[1,2,3,4,1,2,3,1,2]
d={}
m=[]
c=0
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
while c!=len(a):
    r=[]
    for i in d:
        if d[i]!=0:
            c=c+1
            d[i]-=1
            r.append(i)
    m.append(r)
print(m)

# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# print(b,a)
# c=a+b
# c.sort()
# print(c)


a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
i=0
j=0
c=[]
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
if i!=len(a)-1:
    c.extend(a[i:])
if j!=len(b)-1:
    c.extend(b[j:])
print(c)
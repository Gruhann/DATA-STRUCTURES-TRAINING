a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if i not in b:b.append(i)
for i in b:
    print(i,"-",a.count(i))
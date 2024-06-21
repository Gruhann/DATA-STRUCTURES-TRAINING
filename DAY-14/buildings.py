n=list(map(int,input().split()))
i=0
j=len(n)
left=[0]*len(n)
right=[0]*len(n)
m=0
for i in range(len(n)):
    if n[i]>m:
        m=n[i]
    left[i]=m
m1=0
for i in range(len(n)-1,-1,-1):
    if (n[i]>m1):
        m1=n[i]
    right[i]=m1
s=0
for i in range(len(n)):
    s+=abs(min(left[i],right[i])-n[i])
print(s)


        
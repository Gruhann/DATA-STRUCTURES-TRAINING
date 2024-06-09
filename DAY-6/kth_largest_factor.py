n=12
k=2
a=[]
#find factors of k and print kth largest factor
for i in range(k,n//2+1):
    if n%k==0:
        a.append(i)
print(a[-1])
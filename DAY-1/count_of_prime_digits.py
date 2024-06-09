n=int(input())
c=0
while (n):
    if n%10 in [2,3,5,7]:
        c+=1
    n=n/10
print(c)
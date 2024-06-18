from math import sqrt
def isprime(val,i):
    for k in range(i,int(sqrt(val))+1):
        if val%k==0:
            return False
    return True
ip=[4,8,14,22,36,68]
s=0
b=0
for i in range(len(ip)-1):
    for j in range(ip[i+1]-1,ip[i],-1):
        a=isprime(j,2)
        if a==True:
            print(j)
            s+=j
            break
print(s)

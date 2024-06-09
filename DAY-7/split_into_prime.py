
n=int(input())
b=[]
def bc(l, a, i):
    if len(a) == 2 and sum(a)==n:
        b.append(a[:])  
        return
    for j in range(i, n):
        a.append(j)
        bc(l, a, j + 1)
        a.pop() 
    # return b
def isprime(n):
    c=0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            c+=1
            break
    if c==0:
        return True
    return False
bc(n,[],0)
res=[]
print(b)
for i in b:
    if  isprime(i[0]) and isprime(i[1]) :
        res.append(i)
print(res)


# def isprime(x):
#     if(x==1):
#         return 1
#     if(x==2):
#         return 1
#     for i in range(2,(x//2)+1):
#         if(x%i==0):
#             return 0
#     return 1
# a=int(input())
# for i in range(1,(a//2)+1):
#     if (isprime(i)and isprime(a-i)):
#         print("yes")
#         break
# else: 
#     print("No")
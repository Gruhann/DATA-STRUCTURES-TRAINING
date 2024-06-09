
def fun(i,s1,s2):
    if (i==len(a)):
        return s1,s2
    if a[i]%2 == 0:
        s1+=a[i]
    if b[i]%2 != 0:
        s2+=b[i]
    return fun(i+1,s1,s2)
    
# def sum1(a,b):
#     e,o=0,0
#     for i in a:
#        if i%2==0:
#             e+=i
#     for i in b:
#         if i%2!=0:
#             o+=i
#     return e,o 
a=[1,2,3,4,5]
b=[1,2,3,4,5]

c,d=fun(0,0,0)
print(c,d)
# print(sum1(a,b))

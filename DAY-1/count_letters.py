a=input()
c=1
res=''

# res=res+a[0]
# for i in range(len(a)-1):
#     if res[-1]!=a[i]:
#         res=res+a[i]
#     if a[i]==a[i+1]:
#         c+=1
#         i+=1
#     else:
#         res=res+str(c)
#         c=0
#         c+=1
#         i+=1
# res+=str(c)
# print(res)


for i in range(len(a)-1):
    if a[i]==a[i+1]:
        c=c+1
    else:
        res+=a[i]+str(c)
        c=1
res+=a[-1]+str(c)
print(res)

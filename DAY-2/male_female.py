# n=list(map(str,input()))
# if n.count('m')==n.count('f'):
#     print(0)
# elif n.count('m')>n.count('f'):
#     print('m')
# else:
#     print('f')

n=input()
c=0
for i in n:
    if i=='m':
        c+=1
    else:
        c-=1
if c==0:print('0')
elif c>1:print('m')
else:print('f')

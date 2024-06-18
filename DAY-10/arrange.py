def arr(c):
    i=0
    while i<len(c)-2:
        mn=min([c[i],c[i+1],c[i+2]])
        mx=max([c[i],c[i+1],c[i+2]])
        md=sum([c[i],c[i+1],c[i+2]])-mn-mx
        c[i]=mn
        c[i+1]=md
        c[i+2]=mx
        i+=1
    print(c)
ip=[4,9,8,2,14,3,5,6]
arr(ip)
# for i in range(len(ip)):
#     c=ip[i:]
#     c=arr(c)
#     print(c)
#     ip[i:]=c
print(ip)
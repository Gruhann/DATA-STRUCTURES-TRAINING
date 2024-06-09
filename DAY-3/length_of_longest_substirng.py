s=input()
l=len(s)
c=1
max=0
for i in range(l-1):
    if ord(s[i])==ord(s[i+1])-1:
        c+=1
    else:
        if max<c:
            max=c
        c=1
print(max if max else c)
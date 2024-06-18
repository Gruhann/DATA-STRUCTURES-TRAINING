ip=input().split(",")
sol=""
for p in ip:
    i,j=p.split(":")
    l=len(i)
    k=0
    f=0
    if str(l) in j:
        sol+=i[l-1]
    else:
        t=l-1
        while t>0:
            if  str(t) in j:
                sol+=i[t-1]
                f=1
                break
            t-=1
        if f==0:
            sol+='x'
print(sol)
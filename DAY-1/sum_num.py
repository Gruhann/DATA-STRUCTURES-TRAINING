l=list(map(str,input().split()))
o,e,d=0,0,0

for i in l:
    if '.' not in i:
        if int(i)%2==0:
            e+=int(i)
        else:
            o+=int(i)
    else:
        d+=float(i)
    
print(int(o),int(e),d)

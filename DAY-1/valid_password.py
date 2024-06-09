p=input()
if len(p)<7:
    print(8-len(p))
else:
    res=4
    a=0
    b=0
    c=0
    d=0
#upper,lower,special,digit
    for i in p:
        if i.islower():
            a=1 
        if i.isupper():
            b=1 
        if i.isdigit():
            c=1 
        if not i.isalnum():
            d=1
        if a==1 and b==1 and c==1 and d==1:
            print("-1")
            break
    # if a==0 and b==0 and c==0 and d==0:
    #     print("4")
    # elif (a==0 and b==0 and c==0 )or (a==0 and b==0 and d==0 ) or (d==0 and b==0 and c==0 ) or (a==0 and d==0 and c==0 ):
    #     print("3")
    # elif (a==0 and b==0) or (a==0 and c==0) or(a==0 and d==0) or(b==0 and c==0) or(d==0 and b==0) or(c==0 and d==0) :
    #     print("2")
    # elif a==0 or b==0 or c==0 or d==0:
    #     print("1")

m=4-(a+b+c+d)
if(len(p)+m)<8:
    print(8-len(p))
else:
    print(m)



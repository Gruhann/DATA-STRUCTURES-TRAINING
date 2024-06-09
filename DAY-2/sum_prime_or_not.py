n=input()
while True:
    m=sum(list(map(int,list(n))))
    if m>9:
        res=sum(map(int,str(m)))
        print("sum of ", n ,"is", res)
    else:
        res=m
        print("sum of ", n ,"is", res)
    if res in [1,2,3,5,7]:
        print(res,"is prime")
        break
    else:
        print(res ," is not prime ,  checking for ",int(n)+1)
        n = int(n) +1
        n=str(n)



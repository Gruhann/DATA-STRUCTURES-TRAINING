
n=int(input())
while True:
    c=0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            c+=1
            break
    if c==0:
        print(n)
        break
    # else:
    #     while True:
    #         c=0
    #         n+=1
    #         for i in range(2,int(n**0.5)+1):
    #             if(n%i==0):
    #                 c+=1
    #         if c==0:
    #             print("next prime: ", n)
    #             exit()

    else:
        n=n+1
    
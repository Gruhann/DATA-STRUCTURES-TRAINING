# l=[2,3,5,6]
# while True:



def fun(n,target):
    l=[-1]*(target+1)
    l[0]=0
    for i in n:
        for j in range(1,target+1):
            if j>=i:
                if l[j-i]!=-1:
                    if l[j]!=-1 :
                        l[j]=1#not completed and wrong code
                    else:
                        l[j]=l[j-i]+1
    print("yes "if l[-1] else "no ")
                
n=list(map(int,input().split()))
target=int(input())
fun(n,target)


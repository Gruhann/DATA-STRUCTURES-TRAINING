
def fun(n,target):
    l=[-1]*(target+1)
    l[0]=0
    for i in n:
        for j in range(1,target+1):
            if j>=i:
                if l[j-i]!=-1:
                    if l[j]!=-1 :
                        l[j]=min(l[j],l[j-i]+1)
                    else:l[j]=l[j-i]+1
    print(l[-1])
                

n=list(map(int,input().split()))
target=int(input())
fun(n,target)


n=int(input())
if str(n)==str(n)[::-1]:print("yes")
else:
    r=''
    s=str(n)
    l=len(s)
    if l%2==0:
        a=s[:l//2]
        if int(a+a[::-1])>n:
            print(a+a[::-1])
        else:
            q=str(int(a)+1)
            print(q+q[::-1])
    else:
        a=s[:l//2]
        if int(a+s[l//2]+a[::-1])>n:
            print(a+s[l//2]+a[::-1])
        else:
            print(a+str(int(s[l//2])+1)+a[::-1])
            

            


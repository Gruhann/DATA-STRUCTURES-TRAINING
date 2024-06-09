def rev(r,n):
    # r=0
    # while n>0:
    #     r=r*10+n%10
    #     n//=10
    # return r
    if n==0:
        return r
    r=r*10+n%10
    return rev(r,n//10)

n=int(input())
r=rev(0,n)
if n==r:
    print("palidrome")
else:
    print("not palindrome")

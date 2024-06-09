# def add_even(i,s):
#     if i > n:
#         return s
#     # print(i)
#     s+=i
#     return add_even(i+2,s)
# i=0
# n=int(input())
# print(add_even(2,0))

def f(x):
    if x==0: return 0
    return x+f(x-2)
n=13
if n%2==0: 
    print(f(n))
else: print(f(n-1))
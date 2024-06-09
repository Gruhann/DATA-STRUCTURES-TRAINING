a=input()
b=int(input())
# while b>26:
#     b-=26
if b>26:
    b=b%26
for i in a:
    c=ord(i)
    if c-b<97:
        c=c+26
    print(chr(c-b),end="")
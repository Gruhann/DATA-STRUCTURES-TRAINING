a=list(map(int,input().split()))
i=0
j=-1
c=0
while True:
    if a[i]==a[j]:
        break
    c+=1
    i+=1
    j-=1
if c%2 == 0:
    print("even")
else:
    print("odd")

# if len(a)%2 == 0:
#     print("yes")
# else:
#     print("no")
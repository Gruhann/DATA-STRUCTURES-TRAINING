a="ru5gan2l1h8"
b="g5g8gf3jd"
n=[]
for i in a:
    if i.isdigit() and i not in n:
        n.append(i)
for i in b:
    if i.isdigit() and i not in n:
        n.append(i)
print(n)
n.sort(reverse=True)
if int(n[-1])%2!=0:
    for i in range(len(n)-1,-1,-1):
        if int(n[i])%2==0:
            n[i],n[-1]=n[-1],n[i]
            break
n=int("".join(i for i in n))
print(n)
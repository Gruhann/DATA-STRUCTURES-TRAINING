n=int(input())
s=[]
t=[]
u=[]
for i in range(n):
    p,q=input().split(" ")
    if int(p)==1:
        s.append(q)
    if int(p)==2:
        t.append(q)
    if int(p)==3:
        u.append(q)
    if int(p)==4:
        s.remove(q)
        for i in s:
            if q==i:
                s.remove(i)
print(s,t,u)

for i in t:
    if i in s:
        print("True")
    else:
        print("False")
c=0
for i in range(len(u)):
    for j in s:
        if  j.startswith(u[i]):
            c+=1
    print(u[i],"as prefix ",c,"times")
# ip:
# 8
# 1 school
# 1 word
# 1 word
# 1 scholar
# 2 word
# 2 wood
# 3 sch
# 4 word
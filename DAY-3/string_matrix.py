n=int(input())
s=[] 
for i in range(n):
    s.append(list(input()))
a=input()
f=0
for i in range(len(a)):
    if a[i] not in s[i%n]:
        print("no" )
        f=1
        break

else: 
    s[i%n].remove(a[i])

if f==0:print("yes")

# OUTPUT

# 3
# abc
# abc
# def
# aadbbeccf
# yes
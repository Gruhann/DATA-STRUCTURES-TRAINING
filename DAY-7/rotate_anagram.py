s=input()
n=int(input())
l=[input() for i in range(n)]
b=[]
def bc(l, a, i):
    if len(a) == 3 and a not in b:
        b.append(a[:])  
        return
    for j in range(i, len(l)):
        a.append(l[j])
        bc(l, a, j + 1)
        a.pop() 


x=''
bc(s,[],0)
for i in l:
    a=i.split(" ")
    if a[0]=="l" or a[0]=='r':
        x+=s[int(a[1])]
print(b)    
print(x)
f=0
for i in b:
    f=0
    for j in x:
        if j not in i:
            f=1
            break
    if f==0:
       print("yes")
       break
else:
    print("no")
        
    

# print(b)
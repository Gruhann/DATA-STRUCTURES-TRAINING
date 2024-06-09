l=[4,2,2,4,4,2,4,2,2]
# l=[1,2,3,4,5,6,7]
c=1
w=l[0]
for i in range(1,len(l)):
    if l[i]!=w:
        
        c-=1
        if c==0:
            w=l[i]
            c+=1
    else:
        c+=1
print(w)


# l=[2,2,2,1,1,1]
# a=0
# max_length=0
# for i in range(len(l)//2):
#     # a.append(l[i])
#     # for j in range(i,len(l)):
#     #     if l[i]==l[j]:
#     #         c+=1
#     if l.count(l[i])>len(l)//2:
#         max=l.count(l[i])
#         a=l[i]
# print(a if a else 1)
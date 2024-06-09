l=list(map(int,input().split()))
p=0
# for i in range(len(l)-1):
#     for j in range(i+1,len(l)):
#         d=l[j]-l[i]
#         if p<d:
#             p=d
# print(p)
mprofit=0
buy=l[0]
for i in l:
    if i<buy:
        buy=i
    elif i-buy>mprofit:
        mprofit=i-buy

print(mprofit)

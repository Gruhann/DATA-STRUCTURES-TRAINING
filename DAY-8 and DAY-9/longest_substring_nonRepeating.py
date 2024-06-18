s="abfgresagtyuiodfe"
maxc=0
i=0
while i<(len(s)-1) and maxc<len(s)-i :
    j=i
    a=''
    c=0
    while j<len(s)-1:
        a+=(s[j])
        c+=1 
        j+=1
        if s[j] in a:
            i=s[:j].index(s[j])
            break
    print(a,c)
    maxc=c if c>maxc else maxc
    i+=1

print(maxc)


# s="abfgresagtyuiodfe"
# maxc=0
# for i in range(len(s)-1):
#     j=i
#     a=''
#     c=0
#     while j<len(s)-1:
#         a+=(s[j])
#         c+=1 
#         j+=1
#         if s[j] in a:
#             break
#     # print(a,c)
#     maxc=c if c>maxc else maxc
# print(maxc)
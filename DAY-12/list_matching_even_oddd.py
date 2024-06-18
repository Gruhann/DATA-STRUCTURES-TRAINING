
# def fun(l1,l2,l,i,j):
#     while i<len(l1):
#         if l1[i]%2==0:
#             j=0
#             while j<len(l2):
#                 if l2[j]%2!=0:
#                     print(l)
#                     l.append(l1[i]+l2[j])
#                 j+=1
#         i+=1
#     return l

def fun(l1,l2,l,i,j):
    
    def fun2(l1,l2,l,i,j):
        if j>=len(l2):
            i=i+1
            return l
        if l2[j]%2!=0:
            l.append(l1[i]+l2[j])
        return fun2(l1,l2,l,i,j+1)
    
    if i>=len(l1):
        return l
    if l1[i]%2!=0:                    #not completed code
        i+=1
    else:
        fun2(l1,l2,l,i,0)
    fun(l1,l2,l,i+1,0)
    return l


l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
print(fun(l1,l2,[],0,0))

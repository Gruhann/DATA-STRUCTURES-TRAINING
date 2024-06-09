a=input()
# lv='aeiou'
# uv='AEIOU'
# lvc,uvc=0,0
# lc,uc=0,0
# d=0
# s=0
# for i in a:
#     if i in lv:
#         lvc+=1
#     elif i in uv:
#         uvc+=1
#     elif i.islower():
#         if i not in lv:
#             lc+=1
#         elif i not in uv:
#             uc+=1
#     elif i.isdigit():
#         d+=1
#     elif i in '``!@#$%^&*()-_=+/?{}[]':
#         s+=1
# print(lvc)
# print(uvc)
# print(uc)
# print(lc)
# print(d)
# print(s)



uv,lv,uc,lc,d,s=0,0,0,0,0,0
for i in a:
    if i.isupper():
        if i in 'AEIOU':
            uv+=1
        else :uc+1
    elif i.islower():
        if i in 'aeiou':
            lv+=1
        else:
            lc+=1
    elif i.isdigit():
        d+=1
    elif (not i.isalnum()):
        s+=1
        
print(uv,lv,uc,lc,d,s)
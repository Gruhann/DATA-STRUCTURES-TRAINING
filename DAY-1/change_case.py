a=input()
b=''
j=0
for i in a:
    if i in 'aeiouAEIOU':
        if i.islower():
            b+=i.upper()
            j+=1
        else:
            b+=i
            j+=1
    else:
        if i.isupper():
            b+=i.lower()
            j+=1
        else:
            b+=i
            j+=1
   
print(b)

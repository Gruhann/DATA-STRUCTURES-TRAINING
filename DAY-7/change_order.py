n = int(input())
# r=''
for i in range(n):
    order = input()
    s = input()
    result = ''
    for char in order:
        if char in s:
            result+=(char)*s.count(char)
    print(result)

l=[[1,4],[2,3],[6,9],[7,8],[7,9]]
p=[5,6,2,10,9]
max1=0
for i in range(len(l)):
    maxx=p[i]
    c=l[i][1]
    for j in range(len(l)-1):
        if c<=l[j+1][0]:
            maxx=maxx+p[j+1]
            c=l[j+1][1]             
    max1=max(maxx,max1)
print(max1)
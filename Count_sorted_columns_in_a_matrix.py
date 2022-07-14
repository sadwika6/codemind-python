def col(l):
    m=sorted(l)
    n=sorted(l,reverse=True)
    return l==m or l==n
a,b=map(int,input().split())
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
c=0
for j in range(b):
    z=[]
    for i in range(a):
        z.append(m[i][j])
    if col(z):
        c+=1
print(c)
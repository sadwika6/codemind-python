n=int(input())
a=list(map(int,input().split()))
b=[]
k=0
for i in range(n-1):
    j=i+1
    m=0
    for x in range(j,n):
        if a[x]>=m:
            m=a[x]
    b.append(m)
b.append(-1)
print(*b)
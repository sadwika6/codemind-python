n=int(input())
a=list(map(int,input().split()))
k=[]
if n%2==0:
    b=a[:(n//2)]
    c=a[:(n//2)-1:-1]
else:
    b=a[:(n//2)+1]
    c=a[:(n//2):-1]
    c.append(0)
i=0
if n%2==0:
    while i<n//2:
        k.append(b[i])
        k.append(c[i])
        i+=1
else:
    i=0
    while i<(n//2)+1:
        k.append(b[i])
        k.append(c[i])
        i+=1
print(*k)
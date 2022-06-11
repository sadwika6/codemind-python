n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    x=1
    for j in range(n):
        if j!=i:
            x=x*a[j]
    b.append(x)
print(*b)
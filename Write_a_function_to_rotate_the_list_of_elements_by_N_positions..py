n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(k):
    a=l[n-1]
    for j in range(n-2,-1,-1):
        l[j+1]=l[j]
    l[0]=a
print(*l)
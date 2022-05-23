n=int(input())
a=list(map(int,input().split()))
j=n//2
for i in range(n-1,j-1,-1):
    print(a[i],end=' ')
for i in range(j):
    print(a[i],end=' ')
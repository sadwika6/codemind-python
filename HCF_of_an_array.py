n=int(input())
a=list(map(int,input().split()))
a.sort()
k=a[0]
f=0
for i in range(1,n):
    if a[i]%k==0:
        f+=1
if f+1==n:
    print(k)
else:
    print(1)
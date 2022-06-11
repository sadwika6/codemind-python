a=list(map(int,input().split()))
a.sort()
n=len(a)
x=a[n-1]
y=a[n-2]
print((x-1)*(y-1))
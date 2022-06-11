n=int(input())
a=list(map(int,input().split()))
t=int(input())
if t not in a:
    print("-1 -1")
else:
    x=a.index(t)
    for i in range(x,n):
        if a[i]==t:
            y=n-a[::-1].index(t)-1
    print(x,y)
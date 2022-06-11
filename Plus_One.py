n=int(input())
a=list(map(int,input().split()))
if a[n-1]<9:
    a[n-1]+=1
    print(*a)
else:
    s=0
    b=[]
    for i in a:
        s=s*10+i
    s+=1
    while s:
        r=s%10
        b.append(r)
        s//=10
    print(*b[::-1])
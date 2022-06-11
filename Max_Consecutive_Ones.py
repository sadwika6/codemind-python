n=int(input())
a=list(map(int,input().split()))
m=0
c=0
for i in a:
    if i==1:
        c+=1
    else:
        if c>=m:
            m=c
            c=0
if c>m:
    print(c)
else:
    print(m)
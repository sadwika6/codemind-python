n=int(input())
l=list(map(int,input().split()))
x=sum(l[::2])
y=sum(l)-x
d=abs(x-y)
if d%4==0:
    print('X')
else:
    print('Y')
n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
f=0
for i in l:
    if i>=a and i<=b:
        f=1
        print(i,end=' ')
if f==0:
    print(-1)
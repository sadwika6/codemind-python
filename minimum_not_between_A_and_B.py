n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
f=0
for i in l:
    if i<a or i>b:
        s.append(i)
        f=1
if f==1:
    print(min(s))
else:
    print(-1)
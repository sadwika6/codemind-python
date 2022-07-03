n=int(input())
l=list(map(int,input().split()))
k=int(input())
j=[]
f=0
for i in l:
    if l.count(i)==k and i not in j:
        j.append(i)
        f=1
if f==1:
    print(*j)
else:
    print(-1)
n=int(input())
l=list(map(int,input().split()))
k=[]
f=0
for i in l:
    if l.count(i)==i and i not in k:
        k.append(i)
        f=1
if f==1:
    print(*k)
else:
    print(-1)
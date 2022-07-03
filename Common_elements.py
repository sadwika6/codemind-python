n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
k=[]
for i in l1:
    if i in l2:
        k.append(i)
m=[]
for i in k:
    if i not in m:
        m.append(i)
print(*m)
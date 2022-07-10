n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
f=0
for i in l:
    if i<=k:
        c+=1
    if i>k and f==1:
        break
    if i>k and f==0:
        f=1
        continue
print(c)
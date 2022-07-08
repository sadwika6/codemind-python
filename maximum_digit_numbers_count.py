n=int(input())
l=list(map(int,input().split()))
m=0
k=[]
for i in l:
    if len(str(i))>m:
        m=len(str(i))
for i in l:
    if len(str(i))==m:
        k.append(i)
print(*k)
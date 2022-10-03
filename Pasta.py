m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
f=0
for i in b:
    if i in a:
        f+=1
        a.remove(i)
if f==len(b):
    print('Yes')
else:
    print('No')
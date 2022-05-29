n=int(input())
a=list(map(int,input().split()))
b=[]
temp=0
for i in a:
    if i not in b and a.count(i)==1:
        temp=1
        b.append(i)
if temp==1:
    print(*b)
else:
    print("-1")
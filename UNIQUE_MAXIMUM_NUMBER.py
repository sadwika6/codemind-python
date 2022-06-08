n=int(input())
a=list(map(int,input().split()))
x=[]
v=0
for i in a:
    if i not in x and a.count(i)==1:
        x.append(i)
        v=1
if v==1:
    print(max(x))
else:
    print("-1")
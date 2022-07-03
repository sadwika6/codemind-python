n=int(input())
l=list(map(int,input().split()))
l1=[]
k=len(str(l[0]))
for i in l:
    if len(str(i))>k:
        k=len(str(i))
    l1.append(len(str(i)))
print(l1.count(k))
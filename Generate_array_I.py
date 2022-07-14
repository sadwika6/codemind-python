n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(0,n,2):
    l1.append(l[i])
for i in range(1,n+1,2):
    l2.append(l[i])
l3=[]
for i in range(len(l1)):
    for j in range(l2[i]):
        l3.append(l1[i])
print(*l3)
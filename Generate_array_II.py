n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(0,len(l),2):
    for j in range(l[i+1]):
        k.append(l[i])
print(*k)
n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(0,n-1,2):
    for j in range(l[i]):
        r.append(l[i+1])
print(*r)
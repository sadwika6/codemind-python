n=int(input())
l=list(map(int,input().split()))
c=sum(l)//n
k=0
for i in l:
    if i<=c:
        k+=1
print(k)
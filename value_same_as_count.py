n=int(input())
l=list(map(int,input().split()))
k=set(l)
j=0
for i in k:
    if l.count(i)==i:
        j+=1
print(j)
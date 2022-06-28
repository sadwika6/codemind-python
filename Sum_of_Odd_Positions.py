n=int(input())
l=list(map(int,input().split()))
o=0
s=sum(l)
for i in range(0,n,2):
    o+=l[i]
e=s-o
print(e)
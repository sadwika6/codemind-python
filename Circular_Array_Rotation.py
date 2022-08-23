n,k,q=map(int,input().split())
l=list(map(int,input().split()))
res=l[-k:]+l[:-k]
for i in range(q):
    m=int(input())
    print(res[m])
n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    s=str(i)
    s=s[::-1]
    s=int(s)
    k.append(s)
print(*k)
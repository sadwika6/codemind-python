n=int(input())
nums=list(map(int,input().split()))
m=int(input())
index=list(map(int,input().split()))
res=[]
for i in range(n):
    res.insert(index[i],nums[i])
print(*res)
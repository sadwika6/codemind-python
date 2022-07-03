n=int(input())
l=list(map(int,input().split()))
s1=0
for i in range(n//2):
    s1+=l[i]
print(s1)
print(sum(l)-s1)
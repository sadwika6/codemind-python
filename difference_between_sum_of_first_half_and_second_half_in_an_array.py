n=int(input())
l=list(map(int,input().split()))
m=sum(l[:n//2])
n=sum(l[(n//2):])
print(abs(m-n))

def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in l:
    if i<=k and i!=1 and prime(i):
        c+=1
print(c)
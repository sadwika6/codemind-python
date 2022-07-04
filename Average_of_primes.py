def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
k=0
c=0
for i in l:
    if i!=1 and prime(i):
        c+=1
        k+=i
s=k/c
print('%.2f'%s)
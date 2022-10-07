def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=[]
for i in range(n):
    if prime(i):
        l.append(i)
f=0
for i in l:
    for j in l:
        if i!=j and i*j==n:
            print(i,j)
            f=1
    if f==1:
        break
if f==0:
    print(-1)
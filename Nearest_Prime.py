def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    n=int(input())
    for i in range(n,1,-1):
        if prime(i):
            x=i
            break
    for j in range(n,(n*n)+1,1):
        if prime(j):
            y=j
            break
    if n-x<=y-n:
        print(x)
    else:
        print(y)
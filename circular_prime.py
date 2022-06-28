def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input())
s=str(n)
s=s[::-1]
s=int(s)
if prime(n) and prime(s):
    print("circular prime")
elif prime(n) or prime(s):
    print("prime but not a circular prime")
else:
    print("not prime")
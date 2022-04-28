n=int(input())
d=len(str(n))
n1=n*n
d1=n1%(10**d)
if n==d1:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
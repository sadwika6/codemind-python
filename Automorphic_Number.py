n=int(input())
s=len(str(n))
m=n**2
if m%(10**s)==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
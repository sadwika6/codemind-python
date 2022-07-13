n=int(input())
a=[]
b=2
c=2
f=0
for i in range(n):
    a.append(b)
    f=b+c
    b=c
    c=f
print(a[n-1])
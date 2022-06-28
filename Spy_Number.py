n=int(input())
s=str(n)
m=1
k=0
for i in s:
    k+=int(i)
    m*=int(i)
if k==m:
    print("Spy Number")
else:
    print("Not Spy Number")
n=int(input())
s=n*n
s=str(s)
m=0
for i in s:
    m+=int(i)
if m==n:
    print("Neon Number")
else:
    print("Not Neon Number")
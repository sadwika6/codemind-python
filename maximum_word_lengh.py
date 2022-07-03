s=input()
s=s.split()
m=0
for i in s:
    if len(i)>m:
        m=len(i)
print(m)
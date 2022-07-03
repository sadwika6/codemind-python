s=input()
s=s.split()
m=1000
for i in s:
    if len(i)<m:
        m=len(i)
print(m)
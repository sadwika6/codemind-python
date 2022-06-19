s=input()
c=''
s=s.lower()
for i in s:
    if i!=' ' and s.count(i)==1:
        c+=i
x=sorted(c)
y=''
y=y.join(x)
print(y)
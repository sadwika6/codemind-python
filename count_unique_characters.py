s=input()
c=0
s=s.lower()
for i in s:
    if i!=' ' and s.count(i)==1:
        c+=1
print(c)
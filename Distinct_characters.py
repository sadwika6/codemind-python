s=input()
s=s.lower()
c=''
for i in s:
    if s.count(i)==1 and i!=' ':
        c+=i
a=sorted(c)
z=''
z=z.join(a)
z=z.replace(" ","")
print(z)
s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
a=list(s1.split())
b=list(s2.split())
c=0
for i in a:
    if i in b:
        c+=1
print(c)
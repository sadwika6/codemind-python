s=input()
z=0
o=0
for i in s:
    if i=='z':
        z+=1
    if i=='o':
        o+=1
if o==2*z:
    print("Yes")
else:
    print("No")
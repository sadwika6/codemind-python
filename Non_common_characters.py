s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
l=' '
for i in s1:
    if i not in s2 and i not in l:
        l+=i
for i in s2:
    if i not in s1 and i not in l:
        l+=i
if l=='':
    print(-1)
else:
    print(len(l)-1)
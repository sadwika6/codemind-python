s=input()
t=input()
s=list(s)
t=list(t)
s1=[]
t1=[]
for i in s:
    if i=='#':
        s1.pop()
    else:
        s1.append(i)
for i in t:
    if i=='#':
        t1.pop()
    else:
        t1.append(i)
if s1==t1:
    print('True')
else:
    print('False')
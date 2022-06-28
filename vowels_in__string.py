s=input()
c=0
l=[]
for i in s:
    if i in 'aeiouAEIOU' and i not in l:
        l.append(i)
if len(l)!=0:
    print(*l)
else:
    print("-1")
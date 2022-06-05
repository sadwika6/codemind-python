s=input()
a=list(s)
c=0
for i in a:
    if a.count(i)==1:
        c+=1
        print(a.index(i))
        break
if c==0:
    print("-1")
n=input()
n=n.lower()
f=0
for i in 'aeiou':
    if i not in n:
        print(i,end=' ')
        f=1
if f==0:
    print(0)
a=input()
c=1
l=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        c+=1
    else:
        if c>l:
            l=c
        c=1
if c>l:
    l=c
print(l)
s=input()
l=s.split()
c=0
v='aeiouAEIOU'
for i in l:
    a=0
    b=len(i)-1
    while(a<b):
        if (i[a] in v and i[b] not in v) or (i[a] not in v and i[b] in v):
            c+=1
        a+=1
        b-=1
print(c)
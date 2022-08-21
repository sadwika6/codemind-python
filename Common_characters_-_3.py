a=input()
a=a.lower()
s=a.split()
k=[]
y=0
for i in s:
    for j in i:
        y=0
        for x in s:
            if j in x:
                y=1
            else:
                y=0
                break
        if y==1 and j not in k:
            k.append(j)
            
    break
if len(k)>0:
    k.sort()
    print(k[0])
else:
    print(-1)
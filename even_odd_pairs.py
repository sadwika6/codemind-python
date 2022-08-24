n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2!=0:
        o.append(i)
    else:
        e.append(i)
res=[]
i=0
j=0
while i<len(e) or j<len(o):
    if i<len(e):
        res.append(e[i])
        i+=1
    if j<len(o):
        res.append(o[j])
        j+=1
if(n%2!=0):
    res.append(0)
print(*res)
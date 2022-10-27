value={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s=input()
s=s[::-1]
res=0
x=0
for i in s:
    if value[i]<x:
        res-=value[i]
    else:
        res+=value[i]
    x=value[i]
print(res)
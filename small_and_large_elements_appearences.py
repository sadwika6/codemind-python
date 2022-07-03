s=input()
s1=s.split()
mx=max(s)
mn=max(s)
for i in s1:
    for j in i:
        if j<mn:
            mn=j
print(mn,s.count(mn),mx,s.count(mx))
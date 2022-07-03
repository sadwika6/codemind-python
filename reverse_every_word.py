s=input()
s=s.split()
l=[]
for i in s:
    l.append(i[::-1])
print(*l)
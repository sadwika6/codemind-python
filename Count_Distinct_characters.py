s=input()
s=s.lower()
a=set(s)
l=0
for i in a:
    if i==' ':
        l+=1
print(len(a)-l)
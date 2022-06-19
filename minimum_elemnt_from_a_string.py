p=input()
s1=p.split()
s=s1[len(s1)-1]
x=min(s)
if x.isupper():
    if x.lower() in s:
        print(x.lower())
    else:
        print(x)
else:
    print(x)
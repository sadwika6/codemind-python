def value(i):
    if i=='I':
        return 1
    elif i=='V':
        return 5
    elif i=='X':
        return 10
    elif i=='L':
        return 50
    elif i=='C':
        return 100
    elif i=='D':
        return 500
    elif i=='M':
        return 1000
    else:
        return 0
n=input()
s=0
x=0
for i in range(len(n)-1,-1,-1):
    if value(n[i])>=x:
        s+=value(n[i])
    else:
        s-=value(n[i])
    x=value(n[i])
print(s)
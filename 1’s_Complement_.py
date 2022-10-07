a=int(input())
a=bin(a)
a=a[2:]
res=""
for i in a:
    if i=='0':
        res+='1'
    else:
        res+='0'
print(int(res,2))
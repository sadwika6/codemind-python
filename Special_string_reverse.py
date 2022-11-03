s=input()
l=list(s)
alp,spc,ss=[],[],[]
for i in range(len(l)):
    if l[i].isalpha():
        alp.append(l[i])
    else:
        spc.append(l[i])
        ss.append(i)
res=alp[::-1]
for i in range(len(ss)):
    res.insert(ss[i],spc[i])
print("".join(res))
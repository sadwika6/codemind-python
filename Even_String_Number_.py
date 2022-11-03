s=input()
r=''
e=""
o=""
for i in s:
    if i in '0123456789' and i not in r:
        r+=i
    if i in '02468':
        e+=i
    else:
        o+=i
if len(e)==0:
    print(-1)
else:
    o=sorted(o)
    o=o[::-1]
    e=sorted(e)
    e=e[::-1]
    k=e[len(e)-1]
    r=sorted(r)
    r=r[::-1]
    r.remove(k)
    res="".join(r)
    res+=k
    print(res)
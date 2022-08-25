s=input()
s=s.split()
res=""
for i in s:
    k=[]
    for j in i:
        if j not in 'aeiouAEIOU' and j.isalpha():
            k.append(j)
    z=0
    k.sort()
    for j in i:
        if j in 'aeiouAEIOU':
            res+=j
        else:
            res+=k[z]
            z+=1
    res+=" "
res=res[:len(res)-1]
print(res)
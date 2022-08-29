a=input()
v='aeiouAEIOU'
K=[]
for i in a:
    if i in v:
        K.append(i)
k=K[::-1]
j=0
s=''
for i in a:
    if i in v:
        s+=k[j]
        j+=1
    else:
        s+=i
print(s)
s=input()
k=0
f=0
for i in s:
    if i in 'aeiouAEIOU':
        k+=1
    else:
        if k>=f:
            f=k
        k=0
if k>f:
    f=k
print(f)
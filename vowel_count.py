n=input()
n=n.lower()
k=0
for i in n:
    if i in 'aeiou':
        k+=1
print(k)
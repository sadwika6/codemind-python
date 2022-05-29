n=input()
v=0
c=0
d=0
w=0
for i in n:
    if i in 'aeiouAEIOU':
        v+=1
    elif i not in 'AEIOUaeiou0123456789 ':
        c+=1
    elif i in "0123456789":
        d+=1
    elif i in ' ':
        w+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)
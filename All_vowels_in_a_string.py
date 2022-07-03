s=input()
c1=''
c2=''
for i in s:
    if i in 'aeiou' and i not in c1:
        c1+=i
    elif i in 'AEIOU' and i not in c2:
        c2+=i
if len(c1)==5 or len(c2)==5:
    print(True)
else:
    print(False)
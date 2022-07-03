s=input()
c=0
for i in s:
    if ord(i)<65 and i!=' ':
        c+=1
    elif ord(i)>91 and ord(i)<97:
        c+=1
    elif ord(i)>122:
        c+=1
print(c)
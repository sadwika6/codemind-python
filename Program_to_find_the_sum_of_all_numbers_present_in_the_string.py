s=input()
c=0
for i in range(len(s)):
    if s[i] in '0123456789':
        c+=int(s[i])
print(c)
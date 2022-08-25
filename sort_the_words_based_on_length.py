s=input()
s=s.split()
for i in range(len(s)):
    for j in range(len(s)):
        if len(s[i])<len(s[j]) and i!=j:
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
print(*s)
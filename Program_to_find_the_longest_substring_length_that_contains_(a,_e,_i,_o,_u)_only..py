s=input()
m=0
c=0
for i in range(len(s)-1):
    if s[i] in 'aeiouAEIOU' and s[i+1] in 'aeiouAEIOU':
        c+=1
    else:
        c=0
    if c>m:
        m=c
print(m+1)
s=input()
i=0
j=len(s)-1
c=0
while i<j and i!=j:
    if (s[i] in 'AEIOUaeiou' and s[j] not in 'AEIOUaeiou' and s[i]!=' ' and s[j]!=' ') or (s[i] not in 'AEIOUaeiou' and s[j] in 'AEIOUaeiou' and s[i]!=' ' and s[j]!=' '):
        c+=1
        #print(s[i],s[j])
    i+=1
    j-=1
print(c)   
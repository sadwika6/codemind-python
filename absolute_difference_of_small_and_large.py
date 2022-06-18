s=input()
l=s.split()
for i in l:
    print(abs(ord(min(i))-ord(max(i))),end=' ')
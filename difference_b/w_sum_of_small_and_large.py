s=input()
l=s.split()
mn=0
mx=0
for i in l:
    mn+=ord(min(i))
    mx+=ord(max(i))
print(mx-mn)
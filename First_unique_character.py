s=input()
for i in s:
    if i!=' ' and s.count(i)==1:
        print(i)
        break
else:
    print("-1")
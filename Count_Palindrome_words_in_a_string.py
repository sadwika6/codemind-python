def palindrome(n):
    if n==n[::-1]:
        return True
    else:
        return False
s=input()
l=s.split()
c=0
for i in l:
    i=i.lower()
    if palindrome(i):
        c+=1
print(c)
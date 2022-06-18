s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
if sorted(s1)==sorted(s2):
    print("True")
else:
    print("False")
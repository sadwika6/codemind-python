s=input()
s=s.lower()
a=sorted(set(s))
z=''
z=z.join(a)
z=z.replace(" ","")
print(z)
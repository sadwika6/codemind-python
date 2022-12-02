n=int(input())
f=0
if n<1:
    for i in range(-31,0):
        if 2**i==n:
            print('True')
            f=1
            break
if n>1:
    for i in range(0,32):
        if 2**i==n:
            print('True')
            f=1
            break
if f==0:
    print('False')
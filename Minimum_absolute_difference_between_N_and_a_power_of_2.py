n=int(input())
import math
left=pow(2,math.floor(math.log2(n)))
right=left*2
#print(n,left,right)
if n-left<right-n:
    print(n-left)
else:
    print(right-n)
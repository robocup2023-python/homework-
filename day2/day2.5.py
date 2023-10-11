import math


num=0
for i in range(101,201):
    k=int(math.sqrt(i))+1
    for j in range(2,k):
        if i%j == 0:
            num=1
    if num != 1:
        print(i,end=" ")
    num=0
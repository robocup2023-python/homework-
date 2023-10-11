def runnian(a):
    if a % 100 ==0:
        if a % 400 ==0:
            return True
        else:
            return False
    elif a % 4 ==0:
        return True
    else:
        return False

n=int(input("nian"))
y=int(input("yue"))
r=int(input("ri"))
pn=[31,28,31,30,31,30,31,31,30,31,30,31]
num=0
if runnian(n) and y >=3:
    for i in pn[:y-1]:
        num += i
    num += r+1
    print(num)
else:
    for j in pn[:y-1]:
        num += j
    num += r
    print(num)
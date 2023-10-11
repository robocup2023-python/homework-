num=0
x=int(input("shuru"))
a=[1,2,3,4,5,6,7,8,9]
if x >= int(a[-1]):
    a.append(x)
else:
    for i in a:
        if x <= i:
            a.insert(num,x)
            break
    num += 1
print(a)
    
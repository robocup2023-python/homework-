n=int(input("shuliang:"))
num=[]
for i in range(n):
    element=input("shuzi:")
    num.append(element)
m=int(input("m"))
for j in range(m):
    used=num.pop()
    num.insert(0,used)
print(num)
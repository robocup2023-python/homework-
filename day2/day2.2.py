a=int(input("shu"))
k=int(input("ge"))
num=0
for i in range(1,k+1):
    for j in range(0,i):
        num += a*10**j
print(str(num))
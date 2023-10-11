n=int(input('shu'))
print(n,end='=')
for i in range(2,n+1):
    if(n == i):
        print(i)
        break
    elif(n % i == 0):
        while n % i == 0:
            print(i,end="*")
            n=n/i
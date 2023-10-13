def jiwei(a):
    b=[]
    for i in a[::2]:
        b.append(i)
    return(b)
x=list(map(int,input("shuru: ").split()))
print(jiwei(x))
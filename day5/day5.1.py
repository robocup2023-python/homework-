def cacluate(*args):
    average = sum(args)/len(args)
    t=0
    x=[]
    for i in args:
        t+=1
        if i > average:
            x.append(t)
    return (average,x)
a=tuple(map(int,input("shuru: ").split()))
print(cacluate(*a))
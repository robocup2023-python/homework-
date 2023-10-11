h=100
s=100
for i in range(1,11):
    h=h/2
    if i != 10:
        s += h*2
print('Height:',h,'Path:',s)
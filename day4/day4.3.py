x = []
for i in range(3):
    num = []
    for j in range(3):
        element = int(input("shuru matrix1:"))
        num.append(element)
    x.append(num)
y = []
for i in range(3):
    num = []
    for j in range(3):
        element = int(input("shuru matrix2:"))
        num.append(element)
    y.append(num)
z = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        z[i][j] = x[i][j] + y[i][j]
for k in z:
    print(k)
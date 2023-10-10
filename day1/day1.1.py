num=0
for i in range(1,5):
    for j in range(1,5):
        if i != j:
            for k in range(1,5):
                if k != i and k != j:
                    num+=1
print(num)

import random


file_name = "test"
with open(file_name, "w")as file: 
    for i in range(1,11):
        for j in range(1,4):
            x=random.randint(1,100)
            if j <= 2:
                file.write(f"{x},")
            else:
                file.write(f"{x}\n")
lists = []
with open(file_name,'r')as file:
    test_lines = file.read().splitlines()
    for line in test_lines:
        lines = line.split(',')
        lists.append(int(lines[1]))
maxs = max(lists)
mins = min(lists)
average = sum(lists)/10
lists.sort()
mid = (lists[5]+lists[6]) / 2
print(f"max={maxs} min={mins} average={average} mid={mid}")
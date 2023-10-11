line = input("input a line")
num = 0
let = 0
other = 0
spa = 0
for i in line:
    if(i.isalpha()):
        let += 1
    elif(i.isdigit()):
        num += 1
    elif i == ' ':
        spa += 1
    else:
        other +=1
print('Char: ', let,'  Number: ',num,' Other: ',other,'Space: ',spa)
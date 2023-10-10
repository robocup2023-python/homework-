num=[0,1]
a=0
b=1
c=1
for i in range(18):
   num.append(c)
   a=b
   b=c
   c=c+a
print(num)
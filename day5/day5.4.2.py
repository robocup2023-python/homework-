import os

num = 1
path = './img'
file = os.listdir(path)
for i in file:
    if num <= 50:
        old_name = path + '/' + i
        new_name = old_name.replace('.png','.jpg')
        os.rename(old_name,new_name)
    num += 1
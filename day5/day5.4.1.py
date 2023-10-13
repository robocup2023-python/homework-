import os
path='./img'
for i in range(50):
    old_name = f'{path}/{i}.png'
    new_name = f'{path}/{i}.jpg'
    os.rename(old_name, new_name)
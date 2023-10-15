import pathlib
import string
import random
import os
import glob

def text_creat(name,hang):
    file = open("test" + f"/{name}","w")
    for j in range(hang):
        x = " ".join(random.sample((string.ascii_letters + string.digits + string.punctuation),4))
        if j != hang-1:
            file.write(f"{x}\n")
        else:
            file.write(f"{x}")

path = "test"
os.makedirs(path)
i1 = int(input("wenjianshu:"))
j1 = int(input("hangshu:"))
for i in range(i1):
    names = f"test{i}.txt"
    text_creat(names,j1)
test_path = os.path.join(os.getcwd(),'test/*.txt')
test_path = glob.glob(test_path)
for file in test_path:
    x=''
    with open(file,"r") as f:
        for line in f:
            x += line.strip()+"-python\n"
        with open(file,'w') as f:
            f.write(x) 
    old_name = file
    new_name = old_name.replace('.txt','-python.txt')
    os.rename(old_name,new_name)
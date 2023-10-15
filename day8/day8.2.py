#没看懂指哪个程序使用7.5
import pathlib
import string
import random
import os
import glob


def creat(i: int,j: int) -> int:
    path = "test"
    os.makedirs(path)
    for i in range(i):
        name = f"test{i}.txt"
        file = open("test" + f"/{name}","w")
        for j in range(j):
            x = " ".join(random.sample((string.ascii_letters + string.digits + string.punctuation),4))
            if j != j-1:
                file.write(f"{x}\n")
            else:
                file.write(f"{x}")
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
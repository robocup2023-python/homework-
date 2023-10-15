import random
import string


hang = int(input("shuru:"))
file_name = "test.txt"
copy_name = "copy_test.txt"
with open(file_name,"w")as file:
    for i in range(hang):
        x = " ".join(random.sample((string.ascii_letters + string.digits + string.punctuation),4))
        if i != hang-1:
            file.write(f"{x}\n")
        else:
            file.write(f"{x}")
with open(copy_name,"w")as newfile:
    with open(file_name,"r")as file:
        newfile.write(file.read())
print("Finish")
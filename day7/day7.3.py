copy_name = "copy_test.txt"
with open(copy_name,"r+")as file:
    x=file.read()
    file.seek(0)
    file.write('python ')
    file.write(x)
with open(copy_name,"a")as file:
    file.write(' python')
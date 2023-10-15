import os
import glob


test_path = os.path.join(os.getcwd(),'test/*.txt')
test_path = glob.glob(test_path)
for file in test_path:
    with open(file,"r") as f:
        x=f.read()
        if "python" in x:
            x=x.replace("python",'class')
    with open(file,'w') as f:
        f.write(x)
    old_name = file
    if "python" in old_name:
        new_name = old_name.replace('python','class')
        os.rename(old_name,new_name)
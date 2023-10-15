with open('copy_test.txt',"r")as file:
    with open('test.txt',"r")as new_file:
          line1 = file.readline()
          line2 = new_file.readline()
          num = 0
          while line1 or line2:
               num += 1
               if line1 != line2:
                    print(num,end=" ")
               line1 = file.readline()
               line2 = new_file.readline()
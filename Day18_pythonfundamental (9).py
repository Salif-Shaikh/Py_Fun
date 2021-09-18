#Here b34.txt file was created externaly 
#To read a file
with open('b34.txt') as file_obj:
    content = file_obj.read()
print(content)

#we can store the file into a variable
File = 'b34.txt'

with open(File) as f:
    content = f.read()
print(content)

#To show the write function
with open(File,'w') as fw:
    fw.write("This is to show the write function.")

with open(File) as f_obj:
    content = f_obj.read()
print(content)

#To show the append function
with open(File,'a') as fa:
    fa.write("\nThis is to show the append function.")

with open(File) as fi_obj:
    content = fi_obj.read()
print(content)


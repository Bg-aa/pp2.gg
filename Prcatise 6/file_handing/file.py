#ex1
with open("sample.txt","w") as file:
    file.write("Hello, this is the first line\n")
    file.write("This is the second line\n") 

#ex2
with open("sample.txt","r") as file:
    content = file.read()
    print(content)

#ex3
with open("sample.txt","a") as file:
    file.write("Appended line\n")
with open("sample.txt","r") as file:
    content = file.read()
    print(content)

#ex4
import shutil
shutil.copy("sample.txt", "backup.txt")
print("file coppied")

#ex5:
import os
f_name = "sample.txt"
if os.path.exists(f_name):
    os.remove(f_name)
    print("file deleted")
else:
    print("file does not exist")
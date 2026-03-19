#ex1
import os 
os.mkdir("Practice6")
os.makedirs("Practice6/Directory_management/create_list_dirs.py")

#ex2
import os
path = "Practice6"
items = os.listdir(path)
print(items)
for item in items:
    f_path = os.path.join(path,item)
    if os.path.isdir(f_path):
        print(item)
    else:
        print(item)
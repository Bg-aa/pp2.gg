#ex3
import os 
path = "Practise 6"
for root , dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root,file))

#ex4 
import shutil
shutil.copy("Practice6/Directory_management/create_list_dirs.py")
shutil.move("Practice6/Directory_management/create_list_dirs.py")
import os, getpass, os.path
import shutil

user = getpass.getuser()

mypath = 'D:/Users/' + user + '/AppData/Local/Temp'

for root, dirs, files in os.walk(mypath):
    for file in files:
        try:
            os.remove(os.path.join(root, file))
        except:
            print("Failed on " + file)


for root, dirs, files in os.walk(mypath, topdown=False):
    for name in dirs:
        try:
            os.rmdir(os.path.join(root, name))
        except:
            print("Failed on " + name)
    
# print(mypath)
# print(user)
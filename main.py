import os
import shutil

response = input("Are you sure you want to swap the files? (y/n) ")

if response.lower() == "y":

    dir1 = "C:\\Program Files (x86)\\Steam\\userdata"
    dir2 = "C:\\Users\\dawid\\Desktop\\USERDATA"

    files1 = os.listdir(dir1)
    files2 = os.listdir(dir2)

    for f in files1:
        shutil.move(os.path.join(dir1, f), os.path.join(dir2, f))

    for f in files2:
        shutil.move(os.path.join(dir2, f), os.path.join(dir1, f))

    print("\n Successfully swapped the files!\n")

for file in files2:
    print(file)

else:
    print("\n Done...")

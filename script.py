import shutil
import os


def deleteDirectory(array):
    if os.name == "nt":
        path = "D:\\tree\\"
    else:
        path = "D:/tree/"
    for i in array:
        try:
            name = i
            i = path + i
            shutil.rmtree(i)
        except OSError as error:
            print("Error - ", name)
            continue

print("1")
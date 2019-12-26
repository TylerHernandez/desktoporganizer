import shutil, os, os.path
from pathlib import Path

# def organizeDirect(directory, destinationsrc):
#     files = findFiles(directory)
#     #print(list("||" +files+ list("||"))
#     allFiles = os.listdir(destinationsrc)
#     for str(file) in files:
#         type=findType(file)
#         if not findType(file) in allFiles:
#             os.mkdir(destinationsrc+"/"+type)
#         shutil.move(file, destinationsrc+type)
#         print(str(file) + " moved to " + destinationsrc + type)

def bringAlls(directory, strext): # for strext don't include period
    files=findFiles(directory)
    #if the file path does not have a folder named after its extension, lets create it
    try:
        os.mkdir(directory+strext)
    except:
        "This directory already exists"
    directory+=strext
    for file in files:
        if str(file).endswith('.'+strext):#if the file is a (strext)
            shutil.move(str(file), directory)
            print(str(file) + " moved to " + directory)


def findDirectories(directory):
    filePath = Path(directory)
    if filePath.is_dir():
        files = list(x for x in filePath.iterdir() if not(x.is_file()))
    return files

def findFiles(directory):
    filePath = Path(directory)
    if filePath.is_dir():
        files = list(x for x in filePath.iterdir() if x.is_file())
    return files

def findType(file):
    periodloc=0
    file=str(file)
    for i in range(len(file)-1, 0, -1):
        if file[i]=='.':
            periodloc=i
            break
    if periodloc==0:
        return "Error"
    else:
        return file[periodloc+1:]

print(findType("list.png"))

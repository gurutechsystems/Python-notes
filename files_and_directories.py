#use "pathlib" inbuild module to manage files and directories

from pathlib import Path

#Check if  file/folder exists
path= Path('ecommerce') #managing the ecommerce folder
print(path.exists()) #check if folder path exist

#add a folder to a package/directory
#path=Path('email')
#print(path.mkdir())

#remove a folder from a package/directory
#path=Path('email')
#print(path.rmdir())

#Finding all files and folders in a given path
path=Path()
#print(path.glob('*')) # find all files/folders
for file in path.glob('*'):
    print(file)


path=Path()
#print(path.glob('*.*')) # find files only
for file in path.glob('*.*'):
    print(file)


path=Path()
#print(path.glob('*.py')) #all .py files
for file in path.glob('*.py'):
    print(file)

path=Path()
#print(path.glob('*.xml')) #all xml 
for file in path.glob('*.xml'):
    print(file)

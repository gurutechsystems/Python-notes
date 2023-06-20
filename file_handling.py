#we write python codes and store the codes in a file.
#Hence,to access the codes,we have to access the file and the file has access modes such as read/write/create/append/close/delete
#python file handling uses the open() built-in method

"""
Syntax:
f = open(filename, mode)
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

"""

#imports
from os.path import dirname, join
import os

#==>Accessing a file in the read mode
#file_data = open('sample.txt', 'r')
print('\n#access the file using relative path with read access')
file_data=open('test.txt', 'r')
print(file_data.read())

#Accessing a file using absolute path. The path depends on the OS and on the folder, IDE
print('\n#Access a file using absolute path to the file with read access')
file_data=open('C:\\Users\\Admin\\python\\test.txt', 'r') #pwd\filename to get files absolute path and must be "\\"
print(file_data.read())


# Lets try to fix the folder path issue, read the file using automated path
print('\n#Reading files using automated path')
current_dir=dirname(__file__)
file_path=join(current_dir, 'test.txt')
file_data=open(file_path, 'r')
print(file_data.read())

#Read first characters of a file
print('\n#Read first characters of a file')
current_dir=dirname(__file__)
file_path=join(current_dir,'test.txt')
file_data=open(file_path,'r')
print(file_data.read(10))

# read or print one line
print("\n#Read or print one line")
current_dir=dirname(__file__)
file_path=join(current_dir,'test.txt')
file_data=open(file_path,'r')
print(file_data.readline(), end='') #() will print the 1st line of the file.(1/2/3/4 etc) will print the characters in the 1st line. if 1st line is Obase,then (2) will print O and b

#Read or print lines iteratively
print("\n#Read or print lines iteratively")
current_dir=dirname(__file__)
file_path=join(current_dir,'test.txt')
file_data=open(file_path,'r')
for each_line in file_data:
    #print(each_line.split()) 
    print(each_line, end='')

#Get all file lines in a list
print("\n\n# get all file lines in a list")
current_dir=dirname(__file__)
file_path=join(current_dir, "test.txt")
file_data=open(file_path, 'r')
lines_list=file_data.readlines()
print(lines_list)

# close the file after usage
print("\n#Close a file after usage")
current_dir=dirname(__file__)
file_path=join(current_dir, "test.txt")
file_data=open(file_path, 'r')
file_data.close()

# create a new empty file
'''
print("\n# create a new empty file")
current_dir=dirname(__file__)
file_path=join(current_dir, "test2.txt")
file_data=open(file_path, 'x')
file_data.close()
'''

#writing into file i.e modifying a file
print("\n#Modifying a file")
current_dir=dirname(__file__)
file_path=join(current_dir, "test2.txt")
file_data=open(file_path, 'w') #had it been test2.txt did not exist, it will create the file.Hence 'w' can used to create a file with content and also modify an existing file
file_data.write('Hello Ngembane, God is good\n')
file_data.write('welcome to USA\n')           #\n helps u to write in lines
file_data.write('In God we trust')   #Not that 'write' overwrites the existing content in 'w' mode
file_data.close()

#Read written data now
print('\n#Read the file data')
current_dir=dirname(__file__)
file_path=join(current_dir, "test2.txt")
file_data=open(file_path, 'r')
print(file_data.read())
file_data.close()

#Append(add) the content to the existing file
print("\n# append the content to the existing file")
current_dir=dirname(__file__)
file_path=join(current_dir, "test2.txt")
file_data=open(file_path, 'a') #if the file does not exit,it will create the file
file_data.write('\nLuck and Favor is my wish in this country')
#Read file content now
file_data=open(file_path, 'r')
print(file_data.read())
file_data.close()

#Copy file content from one file to another
print("\n# copy a file content to a new file")
    #Open source file in read mode
current_dir=dirname(__file__)
src_file_path=join(current_dir, "test2.txt")
src_file_data=open(src_file_path, 'r')
    #Open/create destination file in write mode
dest_file_path=join(current_dir, "test.txt")
dest_file_data=open(dest_file_path, 'w')
    #Copy content from source to destination file
for line in src_file_data:
    dest_file_data.write(line)

#Close both source and destiantion files
src_file_data.close()
dest_file_data.close()   

#Read destination file content now
dest_file_data=open(dest_file_path, 'r')
print(dest_file_data.read())
dest_file_data.close()   

# deleting a file
print('\n#Delete a file')
current_dir=dirname(__file__)
file_path=join(current_dir, "test2.txt") #if the file does not exist,it will give us an error message(FileNotFoundError)
os.remove(file_path)

# so to avoide such file not found issues we can simply put a conditions
print("\n#verifying if the file exists before deletion")
current_dir = dirname(__file__)
file_path = join(current_dir, "test.txt")
if os.path.exists(file_path):
         os.remove(file_path)
else:
      print('file does not exist')         

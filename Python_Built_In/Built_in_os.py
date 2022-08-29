# Python built-in modules --1.Os

# It is possible to automatically perform many operating system tasks.
# The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
# You first need to import the os module to interact with the underlying operating system. So, import it using the import os statement before using its functions.
import os

#Getting Current Working Directory
#The getcwd() function confirms returns the current working directory.
print("Getting current working directory")
print(os.getcwd())

# Creating a Directory
# By default, if you don't specify the whole path in the mkdir() function, it will create the specified directory in the current working directory or drive.
# The following will create MyPythonProject in the C:\Python37 directory.
print("Make new folder in current directory")
os.mkdir("./newdir")

#Changing Working Directory
os.chdir("./newdir")
print(os.getcwd())
os.chdir("C:/Users/KSS/PycharmProjects/Python_practice")
print(os.getcwd())

#Changing CWD to parent
os.chdir("./newdir")
os.chdir("..") ## change cwd to parent directory
print(os.getcwd())

#Remove directory
#We should the current working directory to the parent directory when we want to delete current directory
#using os.chdir("..") and then remove it using the rmdir() function.
os.rmdir("./newdir")

#Get list directories of CWD

os.listdir()
print(os.listdir())
import sys
#The sys module provides functions and variables used to manipulate different parts of the Python runtime environment.
#Control function and parameters from python interpreter

#명령행에서 인수 전달하기 -- sys.argv

print("You entered: ", sys.argv[1],sys.argv[2],sys.argv[3])

#sys.exit() # Quit interpreter, File termination

#Current directory
print(sys.path())

#sys.maxsize : Returns the largest integer a variable can take

print(sys.maxsize)




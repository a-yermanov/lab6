import os, string

path = r"/Users/anuarermanov/Downloads/dir-and-files/example.txt"
if os.path.exists(path):
    print("The path exists")

    if os.access(path, os.R_OK):
        print("The path is readable")
    else:
        print("The path is not readable")
        
    if os.access(path, os.W_OK):
        print("The path is writable")
    else:
        print("The path is not writible")

    if os.access(path, os.X_OK):
        print("The path is executable")
    else:
        print("The path is not executable")
else:
    print("The path does not exist")
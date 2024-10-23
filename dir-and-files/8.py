import os

if os.path.exists(r"/Users/anuarermanov/Downloads/dir-and-files/example2.txt"):
    os.remove(r"/Users/anuarermanov/Downloads/dir-and-files/example2.txt")
else:
    print("No file")
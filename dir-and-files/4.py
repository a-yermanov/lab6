import os

with open(r"/Users/anuarermanov/Downloads/dir-and-files/example.txt") as path:
    lines = len(path.readlines())
print(lines)
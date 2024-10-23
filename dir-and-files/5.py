import os, string

list = str(input().split())
with open(r"/Users/anuarermanov/Downloads/dir-and-files/example.txt",'w') as here:
    here.write(list)
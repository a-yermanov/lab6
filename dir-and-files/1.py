import os, string

path = os.getcwd()
print(f"Files: {[a for a in os.listdir(path) if os.path.isfile(a)]}, directories: {[b for b in os.listdir(path) if os.path.isdir(b)]} all elements are: {os.listdir(path)}")
with open(r"/Users/anuarermanov/Downloads/dir-and-files/example.txt",'r') as first:
    with open(r"/Users/anuarermanov/Downloads/dir-and-files/example2.txt",'w') as here:
        for line in first:
            here.write(line)
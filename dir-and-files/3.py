import os

here = r"/Users/anuarermanov/Downloads/dir-and-files"
if os.path.exists(here):
    print(os.path.basename(here))
    print(os.path.dirname(here))
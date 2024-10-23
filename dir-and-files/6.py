import os, string

for letter in string.ascii_uppercase:
    with open(letter + ".txt", "w") as here:
        here.writelines(letter)
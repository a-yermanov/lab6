def count(str):
    upper = 0
    lower = 0

    for char in str:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    print(f"Uppercase: {upper}")
    print(f"Lowercase: {lower}")

str = input()
count(str)
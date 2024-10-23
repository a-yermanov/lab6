import math, time

def root(milsec, n):
    time.sleep(milsec/1000)
    return math.sqrt(n)
n = int(input("Sample Input:\n"))
milsec = int(input())
print("Sample Output:")
print(f"Square root of {n} after {milsec} is {root(milsec, n)}")
import os

def dir_1():
    a = os.listdir()
    b = len(a)
    while b > 0:
        print(a[:b])
        b -= 1

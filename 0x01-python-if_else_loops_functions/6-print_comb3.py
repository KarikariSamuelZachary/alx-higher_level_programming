#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if j - 1 <= 0:
            continue
        print("{:d}{:d}".format(i, j), end=", " if i != 8 else '')
print()

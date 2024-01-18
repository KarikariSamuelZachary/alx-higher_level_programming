#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print(f"{len(sys.argv) - 1} argument{'s' if len(sys.argv) != 2 else ''}:")
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")

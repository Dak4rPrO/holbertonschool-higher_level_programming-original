#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    if (len(args) - 1) == 0:
        print(f"{len(args) - 1} arguments.")

    elif (len(args) - 1) == 1:
        print(f"{len(args) - 1} argument:")
        for i in range(len(args) - 1):
            print(f"{i + 1}: {args[i + 1]}")

    elif (len(args) - 1) > 1:
        print(f"{len(args) - 1} arguments:")
        for i in range(len(args) - 1):
            print(f"{i + 1}: {args[i + 1]}")

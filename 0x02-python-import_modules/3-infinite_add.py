#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    resultado = 0

    for x in range(1, len(args)):
        resultado = resultado + int(args[x])
    print(f"{resultado}")

#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lista = dir(hidden_4)

    for j in lista:
        coso = j.startswith('__')
        if not coso:
            print(j)

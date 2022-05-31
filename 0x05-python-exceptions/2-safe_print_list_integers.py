#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    size = 0
    while size < x:
        try:
            print("{}".format(my_list[size]), end="")
        except IndexError:
            break
        size += 1
    print("")
    return size

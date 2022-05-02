#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list.copy()
    if idx < 0 or idx > (len(my_list) - 1):
        return copy_list
    else:
        for x in range(len(copy_list)):
            if x == idx:
                copy_list[x] = element
                return copy_list

#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    uniques = set(my_list)
    res = 0
    for x in uniques:
        res = res + x
    return res

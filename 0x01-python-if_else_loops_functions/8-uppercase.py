#!/usr/bin/python3
def uppercase(str):
    if str >= '97' and str <= '122':
        str = chr(ord(str) - ord('97') + ord('65'))
        print (f'{str}')

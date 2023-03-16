#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    while True:
        try:
            if a < x:
                print(my_list[a], end='')
                a += 1
            else:
                print()
                return a
        except IndexError:
            print()
            return a

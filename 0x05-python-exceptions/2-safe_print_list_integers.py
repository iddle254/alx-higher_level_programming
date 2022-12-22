#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count_init = 0
    count = 0
    while True:
        try:
            if count_init < x:
                print("{:d}".format(my_list[count_init]), end='')
                count_init += 1
                count += 1
            else:
                print()
                return(count)
        except(ValueError, TypeError):
            count_init += 1

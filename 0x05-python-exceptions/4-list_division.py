#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    unit = 0
    while unit < list_length:
        try:
            new_list.append(my_list_1[unit] / my_list_2[unit])
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            unit += 1
    return(new_list)

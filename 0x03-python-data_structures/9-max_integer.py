#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == [[]]:
        return ("None")
    else:
        big_int= my_list[0]
        for i in my_list:
            if i > big_int:
                big_int = i
        print("Max: {:d}".format(big_int))
